def ler_e_retornar_array(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
            
            # Remover quebras de linha, espaços em branco e espaços extras, em seguida, dividir os valores
            valores = conteudo.replace('\n', '').replace(' ', '').split(',')
            
            # Converter os valores para inteiros
            numeros_inteiros = [int(valor) for valor in valores]
            return numeros_inteiros
    except FileNotFoundError:
        print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
        return []