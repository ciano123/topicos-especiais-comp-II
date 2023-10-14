## Esta função é definida para criar um grafo a partir de um arquivo de entrada.
def constroi_grafo_de_arquivo(nomeArquivo):
    grafo = {} # Dicionário para representar o grafo
    
    with open(nomeArquivo, 'r') as arquivo:
        for linha in arquivo: # Itera sobre cada linha do arquivo aberto como leitura 'r'
            linha = linha.strip() 
            if linha.startswith('E '): # verifica as linhas que iniciam com o padrão definido como 'E '
                _, u, v, w = linha.split() # Se obedecer o padrão, cria uma lista de strings ignorando a primeira ocorrencia e as três partes seguintes atribuidas a 'u', 'v' e 'w', vertices conectados e peso respectivamente
                u, v, w = str(u), str(v), int(w) # Conversões de tipos
                
                if u not in grafo: # Verifica se vertice 'u' já existe no grafo
                    grafo[u] = []
                if v not in grafo: # Verifica se vertice 'v' já existe no grafo
                    grafo[v] = []
                
                grafo[u].append((v, w)) # Adiciona a aresta (u,v) a lista de aresta de 'u'
                grafo[v].append((u, w))  # Se o grafo for não-direcionado, adicione a aresta no sentido oposto também

    return grafo # retorna o dicionário grafo, que contém o grafo construído.