def maiorValor1(vetor, instance):
    maior = vetor[0]
    for i in range(1, instance):
        if vetor[i] > maior:
            maior = vetor[i]
    return maior
