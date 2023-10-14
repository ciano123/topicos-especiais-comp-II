def gerar_relatorio(nomeRDiretorio, nome_arquivo, informacoes):
    try:
        # Cria o caminho completo para o arquivo
        caminho_arquivo = f'{nomeRDiretorio}{nome_arquivo}'
        
        # Gera o conteúdo do relatório com base nas informações fornecidas
        conteudo = "\n".join(informacoes)
        
        # Salva o conteúdo no arquivo
        with open(caminho_arquivo, 'w') as arquivo:
            arquivo.write(conteudo)
        
        print(f"Relatório gerado e salvo em '{caminho_arquivo}'.")
    except Exception as e:
        print(f"Ocorreu um erro ao gerar o relatório: {e}")