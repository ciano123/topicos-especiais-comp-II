from data_structure.arvore_binaria import BinaryTree

def Prim_AB(graph, root):
    X = set()
    Q = set(graph.keys())
    pi = {u: None for u in graph}
    
    # Inicialize a árvore binária com chaves infinitas
    key_binary_tree = BinaryTree()
    for u in graph:
        key_binary_tree.insert((float('inf'), u))
    
    key_binary_tree.insert((0, root))  # Defina a chave do vértice raiz como 0
    
    total_weight = 0  # Variável para armazenar o peso total da AGM
    weights = {}  # Dicionário para armazenar os pesos das arestas selecionadas
    
    while Q:
        min_node = key_binary_tree.extract_min()
        if min_node is None:
            break
        
        u = min_node.key[1]
        
        if u in Q:
            Q.remove(u)
        
            if pi[u] is not None:
                X.add((u, pi[u]))
                total_weight += min_node.key[0]
                weights[(u, pi[u])] = min_node.key[0]  # Armazene o peso da aresta
        
            for v, weight in graph[u]:
                if v in Q and weight < key_binary_tree.root.key[0]:
                    key_binary_tree.insert((weight, v))
                    pi[v] = u
    
    return X, total_weight, weights