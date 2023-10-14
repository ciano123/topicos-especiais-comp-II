def busca_sequencial_I(vetor, alvo):
    indice = -1
    for id, elemento in enumerate(vetor):
        if elemento == alvo:
            indice = id
    return indice

def busca_sequencial_II(vetor, alvo):
    for indice, elemento in enumerate(vetor):
        if elemento == alvo:
            return indice  # Elemento encontrado, retornando o índice
    return -1  # Elemento não encontrado 