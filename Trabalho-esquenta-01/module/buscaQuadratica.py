def busca_quadratica(vetor, alvo):
    for i in range(len(vetor)):
        if vetor[i] == alvo:
            return i  # Elemento encontrado, retornando o índice
        for j in range(i + 1, len(vetor)):
            if vetor[j] == alvo:
                return j  # Elemento encontrado, retornando o índice
    return -1  # Elemento não encontrado