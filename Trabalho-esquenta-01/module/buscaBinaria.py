def busca_binaria(valor_inicial, valor_final, vetor, alvo):
    while valor_inicial <= valor_final:
        meio = (valor_inicial + valor_final) // 2
        
        if vetor[meio] == alvo:
            return meio  # Busca elemento do meio, retornando o índice
        elif vetor[meio] < alvo:
            valor_inicial = meio + 1  # Busca na metade direita
        else:
            valor_final = meio - 1  # Busca na metade esquerda
    return -1  # Elemento não encontrado
# if __name__ == '__main__':
#     pesquisa_binaria(valor_inicial, valor_final, vetor, alvo)