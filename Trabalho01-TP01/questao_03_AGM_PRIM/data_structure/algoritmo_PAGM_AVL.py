from data_structure.arvore_AVL import AVLTree

def Prim_AVL(graph):
    # Inicialize a árvore AVL vazia
    tree = AVLTree()
    
    # Escolha um vértice arbitrário como vértice inicial
    start_vertex = list(graph.keys())[0]
    
    # Insira o vértice inicial na árvore com peso zero
    tree.insert(start_vertex, 0)
    
    mst = []  # Lista para armazenar as arestas da árvore geradora mínima
    total_weight = 0  # Variável para armazenar o peso total da AGM
    
    while len(tree) < len(graph):
        min_weight = float('inf')
        min_vertex = None
        
        # Para cada vértice que não está na árvore AVL
        for vertex, edges in graph.items():
            if not tree.contains(vertex):
                # Calcule o peso da menor aresta que o conecta à árvore corrente
                for edge_vertex, weight in edges:
                    if tree.contains(edge_vertex) and weight < min_weight:
                        min_weight = weight
                        min_vertex = vertex
        
        if min_vertex:
            # Remova o vértice com a menor chave (menor peso) da árvore AVL
            tree.delete(min_vertex)
            
            # Adicione o vértice selecionado à árvore corrente
            mst.append((min_vertex, min_weight))
            tree.insert(min_vertex, min_weight)
            
            # Adicione o peso da aresta à variável total_weight
            total_weight += min_weight
    
    return mst, total_weight