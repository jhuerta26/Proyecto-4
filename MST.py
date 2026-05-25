import algorithms as a

def mst():
    # Nodo raiz para algoritmo Dijkstra
    rootNode = 5

    #####################Grafo ErdosRenyi################################

    # Grafo ErdosRenyi de 10 nodos
    grafoErdos = a.randomErdosRenyi(10, 10, directed=False, auto=False)
    mst_kruskal = grafoErdos.KruskalD()
    mst_kruskal.saveGV()
    mst_kruskalI = grafoErdos.Kruskall()
    mst_kruskalI.saveGV()
    mst_prim = grafoErdos.Prim()
    mst_prim.saveGV()

    # Grafo ErdosRenyi de 200 nodos
    grafoErdos = a.randomErdosRenyi(200, 200, directed=False, auto=False)
    mst_kruskal = grafoErdos.KruskalD()
    mst_kruskal.saveGV()
    mst_kruskalI = grafoErdos.Kruskall()
    mst_kruskalI.saveGV()
    mst_prim = grafoErdos.Prim()
    mst_prim.saveGV()
    dijkstra = grafoErdos.Dijkstra(rootNode)
    grafoErdos.saveGVwithLabels()

    #####################Grafo Gilbert####################################

    # Grafo Gilbert de 10 nodos
    grafoGilbert = a.randomGilbert(10, 0.6, directed=False, auto=False)
    mst_kruskal = grafoGilbert.KruskalD()
    mst_kruskal.saveGV()
    mst_kruskalI = grafoGilbert.Kruskall()
    mst_kruskalI.saveGV()
    mst_prim = grafoGilbert.Prim()
    mst_prim.saveGV()

    # Grafo Gilbert de 200 nodos
    grafoGilbert = a.randomGilbert(200, 0.2, directed=False, auto=False)
    mst_kruskal = grafoGilbert.KruskalD()
    mst_kruskal.saveGV()
    mst_kruskalI = grafoGilbert.Kruskall()
    mst_kruskalI.saveGV()
    mst_prim = grafoGilbert.Prim()
    mst_prim.saveGV()
    dijkstra = grafoGilbert.Dijkstra(rootNode)
    grafoGilbert.saveGVwithLabels()

    #####################Grafo Malla################################

    # Grafo Malla de 20 nodos (10x2)
    grafoMalla = a.gridGraph(10, 2, directed=False)
    mst_kruskal = grafoMalla.KruskalD()
    mst_kruskal.saveGV()
    mst_kruskalI = grafoMalla.Kruskall()
    mst_kruskalI.saveGV()
    mst_prim = grafoMalla.Prim()
    mst_prim.saveGV()

    # Grafo Malla de 200 nodos (20x10)
    grafoMalla = a.gridGraph(20, 10, directed=False)
    mst_kruskal = grafoMalla.KruskalD()
    mst_kruskal.saveGV()
    mst_kruskalI = grafoMalla.Kruskall()
    mst_kruskalI.saveGV()
    mst_prim = grafoMalla.Prim()
    mst_prim.saveGV()
    dijkstra = grafoMalla.Dijkstra(rootNode)
    grafoMalla.saveGVwithLabels()

    ###########################Grafo Geografico#######################################

    # Grafo Geografico de 10 nodos
    grafoGeografico = a.randomGeografico(10, 0.5, directed=False, auto=False)
    mst_kruskal = grafoGeografico.KruskalD()
    mst_kruskal.saveGV()
    mst_kruskalI = grafoGeografico.Kruskall()
    mst_kruskalI.saveGV()
    mst_prim = grafoGeografico.Prim()
    mst_prim.saveGV()

    # Grafo Geografico de 200 nodos
    grafoGeografico = a.randomGeografico(200, 0.3, directed=False, auto=False)
    mst_kruskal = grafoGeografico.KruskalD()
    mst_kruskal.saveGV()
    mst_kruskalI = grafoGeografico.Kruskall()
    mst_kruskalI.saveGV()
    mst_prim = grafoGeografico.Prim()
    mst_prim.saveGV()
    dijkstra = grafoGeografico.Dijkstra(rootNode)
    grafoGeografico.saveGVwithLabels()

    #####################Grafo BarabasiAlbert################################

    # Grafo BarabasiAlbert de 10 nodos
    grafoBarabasiAlbert = a.randomBarabasiAlbert(10, 5, directed=False, auto=False)
    mst_kruskal = grafoBarabasiAlbert.KruskalD()
    mst_kruskal.saveGV()
    mst_kruskalI = grafoBarabasiAlbert.Kruskall()
    mst_kruskalI.saveGV()
    mst_prim = grafoBarabasiAlbert.Prim()
    mst_prim.saveGV()

    # Grafo BarabasiAlbert de 200 nodos
    grafoBarabasiAlbert = a.randomBarabasiAlbert(200, 3, directed=False, auto=False)
    mst_kruskal = grafoBarabasiAlbert.KruskalD()
    mst_kruskal.saveGV()
    mst_kruskalI = grafoBarabasiAlbert.Kruskall()
    mst_kruskalI.saveGV()
    mst_prim = grafoBarabasiAlbert.Prim()
    mst_prim.saveGV()
    dijkstra = grafoBarabasiAlbert.Dijkstra(rootNode)
    grafoBarabasiAlbert.saveGVwithLabels()

    #####################Grafo DorogovtsevMendes################################

    # Grafo DorogovtsevMendes de 10 nodos
    grafoDorogovt = a.randomDorogovtsevMendes(n=10, directed=False)
    mst_kruskal = grafoDorogovt.KruskalD()
    mst_kruskal.saveGV()
    mst_kruskalI = grafoDorogovt.Kruskall()
    mst_kruskalI.saveGV()
    mst_prim = grafoDorogovt.Prim()
    mst_prim.saveGV()

    # Grafo DorogovtsevMendes de 200 nodos
    grafoDorogovt = a.randomDorogovtsevMendes(n=200, directed=False)
    mst_kruskal = grafoDorogovt.KruskalD()
    mst_kruskal.saveGV()
    mst_kruskalI = grafoDorogovt.Kruskall()
    mst_kruskalI.saveGV()
    mst_prim = grafoDorogovt.Prim()
    mst_prim.saveGV()
    dijkstra = grafoDorogovt.Dijkstra(rootNode)
    grafoDorogovt.saveGVwithLabels()