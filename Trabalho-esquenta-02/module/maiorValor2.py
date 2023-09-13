def maiorValor2(vetor, valor_inicial, valor_final):
    if (valor_final - valor_inicial <= 1):
        return max(vetor[valor_inicial], vetor[valor_final])
    else:
        media = int((valor_inicial + valor_final)/2)
        var1 = maiorValor2(vetor, valor_inicial, media)
        var2 = maiorValor2(vetor, media+1, valor_final)

        return max(var1, var2)