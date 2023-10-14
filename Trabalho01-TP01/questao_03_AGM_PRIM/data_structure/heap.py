class FibonacciHeapNode:
    def __init__(self, key, vertex):
        self.key = key
        self.vertex = vertex
        self.degree = 0
        self.marked = False
        self.parent = None
        self.child = None
        self.next = self
        self.prev = self


class FibonacciHeap:
    def __init__(self):
        self.min_node = None
        self.node_count = 0

    def insert(self, key, vertex):
        new_node = FibonacciHeapNode(key, vertex)
        if self.min_node is None:
            self.min_node = new_node
        else:
            self._link(self.min_node, new_node)
            if key < self.min_node.key:
                self.min_node = new_node
            elif key == self.min_node.key and vertex < self.min_node.vertex:
                self.min_node = new_node
        self.node_count += 1

    def extract_min(self):
        min_node = self.min_node
        if min_node:
            if min_node.child:
                child = min_node.child
                while True:
                    next_child = child.next
                    child.prev = min_node.prev
                    child.next = min_node.next
                    min_node.prev.next = child
                    min_node.next.prev = child
                    child.parent = None
                    if next_child == min_node.child:
                        break
                    child = next_child
            min_node.prev.next = min_node.next
            min_node.next.prev = min_node.prev
            if min_node == min_node.next:
                self.min_node = None
            else:
                self.min_node = min_node.next
                self._consolidate()
            self.node_count -= 1
        return min_node.vertex if min_node else None

    def _link(self, node1, node2):
        node1.next.prev = node2.prev
        node2.prev.next = node1.next
        node1.next = node2
        node2.prev = node1

    def _consolidate(self):
        max_degree = int(self.node_count ** 0.5) + 1
        roots = [None] * max_degree

        current = self.min_node
        unprocessed_nodes = [current]

        while unprocessed_nodes:
            current = unprocessed_nodes.pop()
            degree = current.degree

            while roots[degree]:
                other = roots[degree]
                if current.key > other.key:
                    current, other = other, current
                self._link(current, other)
                roots[degree] = None
                degree += 1

            roots[degree] = current

        self.min_node = None
        for root in roots:
            if root:
                if self.min_node is None:
                    self.min_node = root
                elif root.key < self.min_node.key:
                    self.min_node = root


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, edges):
        self.graph[u] = edges
        self.graph[u].sort(key=lambda x: x[1])  # Ordenar as arestas por peso

    def prim_mst(self):
        heap = FibonacciHeap()
        in_mst = {vertex: False for vertex in self.graph}
        key = {vertex: float('inf') for vertex in self.graph}
        parent = {vertex: -1 for vertex in self.graph}

        # Adiciona o primeiro vértice à heap
        start_vertex = list(self.graph.keys())[0]
        heap.insert(float('-inf'), start_vertex)
        key[start_vertex] = 0

        while heap.node_count > 0:
            u = heap.extract_min()
            in_mst[u] = True

            for v, weight in self.graph[u]:
                if not in_mst[v] and weight < key[v]:
                    key[v] = weight
                    parent[v] = u
                    heap.insert(weight, v)

        return parent


def constroi_grafo_de_arquivo(nomeArquivo):
    grafo = {}  # Dicionário para representar o grafo

    try:
        with open(nomeArquivo, 'r') as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                if linha.startswith('E '):
                    partes = linha.split()

                    # Verifique se há pelo menos 4 partes antes de tentar desempacotar
                    if len(partes) >= 4:
                        _, u, v, w = partes
                        u, v, w = str(u), str(v), int(w)

                        # Certifique-se de que 'u' e 'v' são strings
                        if u not in grafo:
                            grafo[u] = []
                        if v not in grafo:
                            grafo[v] = []

                        grafo[u].append((v, w))
                        grafo[v].append((u, w))
                        grafo[u].sort(key=lambda x: x[1])  # Ordenar as arestas por peso
                        grafo[v].sort(key=lambda x: x[1])  # Ordenar as arestas por peso
    except FileNotFoundError:
        print(f"Erro: O arquivo {nomeArquivo} não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

    return grafo


if __name__ == "__main__":
    # Nome do arquivo STP
    nomeArquivo = r'C:\Users\alex1\OneDrive\Documentos\Mestrado\2023.2\ESPECIAL\trab01\AGM0\ALUT\alut0805.stp'  # Substitua pelo caminho real

    # Construir o grafo a partir do arquivo
    g = Graph()
    g.graph = constroi_grafo_de_arquivo(nomeArquivo)

    # Encontrar a AGM com Prim
    mst_parent = g.prim_mst()


    # Calcular o peso total da AGM
    total_peso_agm = sum(weight for v, u in mst_parent.items() if u != -1
                        for neighbor, weight in g.graph[u] if neighbor == v)

    # Imprimir as arestas e pesos
    print("Aresta - Peso")
    for v, u in mst_parent.items():
        if u != -1:
            # Encontrando o peso da aresta
            weight = next(weight for neighbor, weight in g.graph[u] if neighbor == v)
            print(f"{u} - {v} : {weight}")

    # Imprimir o peso total da AGM
    print(f"Peso total da Árvore Geradora Mínima: {total_peso_agm}")