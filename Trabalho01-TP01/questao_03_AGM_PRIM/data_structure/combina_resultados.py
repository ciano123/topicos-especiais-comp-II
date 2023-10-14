import os, csv, re

def combinar_csv(diretorio, parte_nome):
    # Verifica se o diretório existe
    if not os.path.exists(diretorio):
        print(f"Diretório {diretorio} não encontrado.")
        return

    # Lista de arquivos CSV no diretório
    arquivos_csv = [arquivo for arquivo in os.listdir(diretorio) if arquivo.endswith('.csv')]

    # Verifica se existem arquivos CSV no diretório
    if not arquivos_csv:
        print(f"Não foram encontrados arquivos CSV em {diretorio}.")
        return

    # Caminho completo para o arquivo "results.csv"
    caminho_resultados = os.path.join(diretorio, 'results.csv')
    # Converte para minuscula
    parte_nome = parte_nome.lower()
    # Abre o arquivo "results.csv" em modo de escrita
    with open(caminho_resultados, 'w', newline='') as arquivo_resultados:
        escritor_csv = csv.writer(arquivo_resultados)

        # Itera sobre cada arquivo CSV e copia seus dados para o arquivo "results.csv"
        for arquivo_csv in arquivos_csv:
            caminho_arquivo_csv = os.path.join(diretorio, arquivo_csv)

            # Encontra a parte do nome do arquivo que contém "alue"
            match = re.search(rf'{parte_nome}(\d+)', arquivo_csv)
            if match:
                nome_arquivo = f"Arquivo: {parte_nome}{match.group(1)}"
            else:
                nome_arquivo = "Arquivo: Desconhecido"

            # Escreve o nome do arquivo no "results.csv"
            escritor_csv.writerow([nome_arquivo])

            with open(caminho_arquivo_csv, 'r') as arquivo_csv_atual:
                leitor_csv = csv.reader(arquivo_csv_atual)
                for linha in leitor_csv:
                    escritor_csv.writerow(linha)
                
                # Adiciona uma linha em branco após cada arquivo CSV
                escritor_csv.writerow([])

    print(f"Os dados dos arquivos CSV foram combinados em {caminho_resultados}.")