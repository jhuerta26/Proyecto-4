from node import Node
from edge import Edge
from queue import PriorityQueue
import math

class Graph:
    def __init__(self,id="grafo", directed=False, auto=False):
        """
        Constructor
        """
        self.id=id
        self.nodes={}
        self.edges={}
        self.directed= directed
        self.auto=auto


    def addNode(self, id):
        """
        Agrega nodo al grafo, en caso de que no exista lo crea, si existe, regresa el nodo
        encontrado en el diccionario
        :param id= Node Id
        :return: node
        """
        new_node=self.nodes.get(id)
        if new_node is None:
            new_node=Node(id)
            self.nodes[new_node.id]=new_node
        return new_node

    def addEdge(self, source, target):
        """
        Agregar una arista al grafo, los nodos deben ser agregados con anterioridad, si no,
        levanta una excepcion
        :param source: Node source
        :param target: Node target
        """

        #Si los nodos no se encuentran en el grafo, levantar excepcion
        if self.nodes.get(source) is None or self.nodes.get(target) is None:
            raise Exception("Nodos no encontrados en el grafo, por favor agregarlos primero")

        #nodos en grafo
        nodeSource=self.nodes[source]
        nodeTarget=self.nodes[target]

        #crear el id de la arista
        idAux=str(source)+' -> '+str(target)

        #Si el grafo es no dirigido, checar que no se repitan los vertices en el diccionario
        repeated=False
        autoAux=False
        if not self.directed:
            idAuxNotDirected=str(target) + ' -> ' +str(source)
            aux=self.edges.get(idAuxNotDirected)
            if not(aux is None):
                repeated=True
        
        #Si el grafo es no autociclico, checar que source y target no sean iguales
        if not self.auto:
            if source is target:
                #print(source, target)
                autoAux=True
        
        new_edge= self.edges.get(idAux)
        
        """
        chequeo para grafo no dirigido y no autociclico.
        si la arista es nueva (no se encuentra en el grafo) y los nodos no son repetidos
        agrega nueva arista
        """
        if new_edge is None and repeated is False and autoAux is False:
            new_edge= Edge(idAux, nodeSource, nodeTarget)
            self.edges[new_edge.id]=new_edge
            nodeSource.attr.get("neighbors").append(nodeTarget)
            nodeTarget.attr.get("neighbors").append(nodeSource)
            nodeSource.attr.get("edges").append(new_edge)
            nodeTarget.attr.get("edges").append(new_edge)
            
        return new_edge


    def getDegree(self, id):
        """
        Obtener el grado de nodo
        :param: id: Node id
        :return: Node degree
        """
        node=self.nodes.get(id)
        if node is None:
            return 0
        return len(node.attr["neighbors"])
    
    def getNode(self, id):
        """
        Encontrar nodo en el grafo
        :param id: Node id to find
        :return: found node
        """
        return self.nodes.get(id)

    def getTotalNodes(self):
        """
        Obtener el total de nodos en el grafo
        :return: total nodes
        """
        nodes=self.nodes
        if nodes is None:
            return 0
        return len(self.nodes)
    
    def getTotalEdges(self):
        """
        Obtener el total de aristas del grafo
        :return: total edges
        """
        edges=self.edges
        if edges is None:
            return 0
        return len(self.edges)
    
    ######GV files######
    def saveGV(self):
        """
        Crea el archivo .gv que posteriormente sera usado para la creacion de los grafos
        """

        #creacion del string gv
        graph=''
        graph+='digraph '+self.id+' {\n'
        
        for nodo in self.nodes:
            graph+=str(nodo)+';\n'

        for key, value in self.edges.items():
            graph+= value.id+';\n'

        graph+='}'

        #se escribe y salva el archivo
        name=self.id+'.gv'
        file = open(name, "w")
        file.write(graph)
        file.close()
        #se imprime q el file fue creado para saber cuando termina
        print('File GraphViz: '+name+' was created\n')
    

    def saveGVwithLabels(self):

        graph = ''
        graph += 'digraph ' + self.id + ' {\n'

        # Nodos: ID fijo (nodo_i) y label con distancia
        for key, value in self.nodes.items():
            node_id = f'nodo_{value.id}'
            label = f'{node_id} ({value.attr["distance"]})'
            graph += f'"{node_id}" [label="{label}"];\n'

        # Aristas: usan solo los IDs de los nodos; el peso va en [weight=...]
        for key, value in self.edges.items():
            source_id = f'nodo_{value.source.id}'
            target_id = f'nodo_{value.target.id}'
            weight = value.attr["weight"]
            graph += f'"{source_id}" -> "{target_id}" [weight={weight}];\n'

        graph += '}'

        name = self.id + '.gv'
        with open(name, 'w') as f:
            f.write(graph)

        print('File GraphViz: ' + name + ' was created\n')

    #########Proyecto 3 - Algoritmo de Dijkstra###############


    def setEdgeWeight(self,weight, source, target):
        """
        Funcion que asigna el peso de una arista
        :param weight: peso
        :param source: nodo fuente
        :param target: nodo objetivo
        """
        #crear el id de la arista
        idAux=str(source)+' -> '+str(target)
        #obtener la arista objeto
        aux=self.edges.get(idAux)
        #si arista existe
        if aux is not None:
            #asignar a la arista el peso
            aux.attr["weight"]=weight

    def Dijkstra(self, rootNode):
        """
        Algoritmo de Dijkstra desde un nodo raíz.
        Asigna distancias mínimas a cada nodo y devuelve el mismo grafo.
        :param rootNode: id del nodo raíz
        :return: self (grafo con distancias actualizadas)
        """
        # Inicializar distancias e parent de todos los nodos
        for node in self.nodes.values():
            node.attr["distance"] = float('inf')
            node.attr["parent"] = None

        start = self.nodes.get(rootNode)
        if start is None:
            print(f"Nodo raíz {rootNode} no encontrado en el grafo.")
            return self

        start.attr["distance"] = 0

        pq = PriorityQueue()
        pq.put((0, rootNode))

        visited = set()

        while not pq.empty():
            dist, u_id = pq.get()
            if u_id in visited:
                continue
            visited.add(u_id)

            u = self.nodes[u_id]
            for edge in u.attr["edges"]:
                # Identificar el vecino (grafo no dirigido)
                v = edge.target if edge.source.id == u_id else edge.source
                weight = edge.attr["weight"]
                new_dist = dist + weight

                if new_dist < v.attr["distance"]:
                    v.attr["distance"] = new_dist
                    v.attr["parent"] = u_id
                    pq.put((new_dist, v.id))

        return self

        ######### Proyecto 4 - Árbol de Expansión Mínima: Kruskal directo ###########
    def KruskalD(self):
        """
        Algoritmo de Kruskal directo.
        Devuelve un grafo que representa el Árbol de Expansión Mínima (MST)
        y muestra en consola el peso total del MST.
        """
        # Nombre del grafo MST
        name = self.id + "_KruskalD_MST"
        mst = Graph(name, directed=self.directed, auto=self.auto)

        # Agregar todos los nodos al grafo MST (sin aristas al inicio)
        for node_id in self.nodes.keys():
            mst.addNode(node_id)

        # Estructuras de Union-Find (Disjoint Set)
        parent = {}
        rank = {}

        def find(x):
            # Búsqueda con compresión de caminos
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            # Unión por rango
            rx = find(x)
            ry = find(y)
            if rx == ry:
                return
            if rank[rx] < rank[ry]:
                parent[rx] = ry
            elif rank[rx] > rank[ry]:
                parent[ry] = rx
            else:
                parent[ry] = rx
                rank[rx] += 1

        # Inicializar conjuntos
        for node_id in self.nodes.keys():
            parent[node_id] = node_id
            rank[node_id] = 0

        # Ordenar aristas por peso (menor a mayor)
        edges_sorted = sorted(self.edges.values(), key=lambda e: e.attr["weight"])

        total_weight = 0

        # Recorrer aristas en orden creciente
        for edge in edges_sorted:
            u = edge.source.id
            v = edge.target.id
            if find(u) != find(v):
                # Agregar arista al MST
                mst.addEdge(u, v)
                mst.setEdgeWeight(edge.attr["weight"], u, v)
                # Unir componentes
                union(u, v)
                # Acumular peso
                total_weight += edge.attr["weight"]

        print(f"[KruskalD] Peso total del MST: {total_weight}")
        return mst

        ######### Proyecto 4 - Árbol de Expansión Mínima: Kruskal inverso ###########
    def Kruskall(self):
        """
        Algoritmo de Kruskal inverso.
        Empieza con todas las aristas y va eliminando las más pesadas
        siempre que el grafo permanezca conectado.
        Devuelve el grafo MST y muestra el peso total.
        """
        # Conjunto de IDs de todas las aristas que actualmente "se conservan"
        edges_keep = set(self.edges.keys())

        # Aristas ordenadas de mayor a menor peso
        edges_desc = sorted(self.edges.values(),
                            key=lambda e: e.attr["weight"],
                            reverse=True)

        node_ids = list(self.nodes.keys())
        if not node_ids:
            return None

        # Función auxiliar para probar si el grafo sigue conectado
        # usando solamente las aristas de edges_keep (menos la candidata a borrar)
        def is_connected_without(edge_to_remove_id):
            # Construir lista de aristas efectivamente disponibles
            usable_edges = [self.edges[eid] for eid in edges_keep
                            if eid != edge_to_remove_id]

            # Si no hay aristas pero hay más de 1 nodo, no está conectado
            if len(usable_edges) == 0:
                return len(node_ids) <= 1

            # Construir una lista de adyacencias temporal
            adj = {nid: [] for nid in node_ids}
            for e in usable_edges:
                u = e.source.id
                v = e.target.id
                adj[u].append(v)
                adj[v].append(u)

            # Hacer BFS/DFS desde el primer nodo
            start = node_ids[0]
            visited = set([start])
            stack = [start]
            while stack:
                u = stack.pop()
                for v in adj[u]:
                    if v not in visited:
                        visited.add(v)
                        stack.append(v)

            # Conectado si visitamos todos los nodos
            return len(visited) == len(node_ids)

        # Probar eliminar cada arista, de la más pesada a la más ligera
        for edge in edges_desc:
            eid = edge.id
            # Probar si podemos quitar esta arista manteniendo conectividad
            if is_connected_without(eid):
                edges_keep.remove(eid)

        # Con edges_keep ya tenemos sólo las del MST
        name = self.id + "_KruskalInv_MST"
        mst = Graph(name, directed=self.directed, auto=self.auto)

        # Agregar nodos
        for nid in node_ids:
            mst.addNode(nid)

        total_weight = 0
        # Agregar sólo las aristas que quedaron
        for eid in edges_keep:
            e = self.edges[eid]
            u = e.source.id
            v = e.target.id
            mst.addEdge(u, v)
            mst.setEdgeWeight(e.attr["weight"], u, v)
            total_weight += e.attr["weight"]

        print(f"[Kruskal inverso] Peso total del MST: {total_weight}")
        return mst

        ######### Proyecto 4 - Árbol de Expansión Mínima: Prim ######################
    def Prim(self):
        """
        Algoritmo de Prim.
        Devuelve un grafo que representa el Árbol de Expansión Mínima (MST)
        y muestra el peso total del MST.
        """
        if not self.nodes:
            return None

        # Elegir un nodo cualquiera como raíz inicial
        start_id = next(iter(self.nodes.keys()))

        name = self.id + "_Prim_MST"
        mst = Graph(name, directed=self.directed, auto=self.auto)

        # Agregar todos los nodos
        for nid in self.nodes.keys():
            mst.addNode(nid)

        visited = set()
        visited.add(start_id)

        # Cola de prioridad de aristas (peso, u, v)
        pq = PriorityQueue()

        # Agregar aristas que salen del nodo inicial
        start_node = self.nodes[start_id]
        for e in start_node.attr["edges"]:
            u = e.source.id
            v = e.target.id
            # identificar el otro extremo
            w = v if u == start_id else u
            pq.put((e.attr["weight"], start_id, w))

        total_weight = 0

        # Mientras haya aristas posibles y queden nodos sin visitar
        while not pq.empty() and len(visited) < len(self.nodes):
            weight, u, v = pq.get()
            if v in visited and u in visited:
                # ambos extremos ya están, esta arista crearía ciclo
                continue

            # determinar cuál es el nuevo nodo que se incorpora
            new_node = v if v not in visited else u
            old_node = u if new_node == v else v

            # Marcar como visitado
            visited.add(new_node)

            # Agregar arista al MST
            mst.addEdge(old_node, new_node)
            mst.setEdgeWeight(weight, old_node, new_node)
            total_weight += weight

            # Agregar nuevas aristas que salen del nuevo nodo
            node_obj = self.nodes[new_node]
            for e in node_obj.attr["edges"]:
                x = e.source.id
                y = e.target.id
                other = y if x == new_node else x
                if other not in visited:
                    pq.put((e.attr["weight"], new_node, other))

        print(f"[Prim] Peso total del MST: {total_weight}")
        return mst