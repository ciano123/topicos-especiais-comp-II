import csv
import os

def gerar_relatorio(nomeRDiretorio, nome_arquivo, informacoes):
    try:
        # Remove a extensão .stp do nome do arquivo e adiciona .csv
        nome_arquivo_sem_extensao = os.path.splitext(nome_arquivo)[0]
        nome_arquivo_csv = f'{nome_arquivo_sem_extensao}.csv'
        
        # Cria o caminho completo para o arquivo CSV
        caminho_arquivo = os.path.join(nomeRDiretorio, nome_arquivo_csv)
        
        # Abre o arquivo CSV para escrita
        with open(caminho_arquivo, mode='w', newline='') as arquivo_csv:
            writer = csv.writer(arquivo_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            
            # Escreve as informações no arquivo CSV
            for linha in informacoes:
                writer.writerow([linha])  # Cada linha é uma lista de valores (uma única célula neste caso)
        
        print(f"Relatório gerado e salvo em '{caminho_arquivo}'.")
    except Exception as e:
        print(f"Ocorreu um erro ao gerar o relatório: {e}")