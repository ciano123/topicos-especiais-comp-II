def busca_ternaria(vetor, alvo):
    esquerda = 0
    direita = len(vetor) - 1
    
    while esquerda <= direita:
        terco1 = esquerda + (direita - esquerda) // 3
        terco2 = direita - (direita - esquerda) // 3
        
        if vetor[terco1] == alvo:
            return terco1
        if vetor[terco2] == alvo:
            return terco2
        
        if alvo < vetor[terco1]:
            direita = terco1 - 1
        elif alvo > vetor[terco2]:
            esquerda = terco2 + 1
        else:
            esquerda = terco1 + 1
            direita = terco2 - 1
            
    return -1