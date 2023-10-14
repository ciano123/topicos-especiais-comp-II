def busca_cubica(vetor, alvo):
    for i in range(len(vetor)):
        for j in range(i, len(vetor)):
            for k in range(j, len(vetor)):
                if vetor[i] + vetor[j] + vetor[k] == alvo:
                    return i, j, k  # Elementos encontrados, retornando índices
    return -1, -1, -1  # Elementos não encontrados