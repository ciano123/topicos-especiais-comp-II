import re
import pandas as pd

def gera_dados_finais(diretorio, current_inst, current_tree):

    # Lê o arquivo "results.csv" em um DataFrame
    df = pd.read_csv(f'{diretorio}/results.csv', header=None, names=['Dados'])


    # Inicializa listas para armazenar os dados resumidos
    nomes_arquivos = []
    tempos_medios = []
    memorias_medias = []

    # Variáveis temporárias para armazenar informações de cada arquivo
    nome_arquivo = None
    tempo_medio = None
    memoria_media = None

    # Itera pelas linhas do DataFrame
    for linha in df['Dados']:
        if linha.startswith('Arquivo: '):
            if nome_arquivo is not None:
                # Armazena informações do arquivo atual nas listas
                nomes_arquivos.append(nome_arquivo)
                tempos_medios.append(tempo_medio)
                memorias_medias.append(memoria_media)
            
            # Inicializa variáveis temporárias com os novos valores
            nome_arquivo = linha.split('Arquivo: ')[1].strip()
            tempo_medio = None
            memoria_media = None
        elif linha.startswith('Tempo Medio: '):
            tempo_medio = re.search(r'\d+\.\d+', linha).group(0)
        elif linha.startswith('Memoria Media: '):
            memoria_media = re.search(r'\d+\.\d+', linha).group(0)

    # Certifique-se de armazenar os últimos valores
    if nome_arquivo is not None:
        nomes_arquivos.append(nome_arquivo)
        tempos_medios.append(tempo_medio)
        memorias_medias.append(memoria_media)

    # Converte os valores de tempo e memória para float
    tempos_medios = [float(tempo) for tempo in tempos_medios]
    memorias_medias = [float(memoria) for memoria in memorias_medias]

    # Cria um DataFrame final com os dados resumidos
    data = {'Nome do arquivo': nomes_arquivos, 'Tempo médio': tempos_medios, 'Memoria media': memorias_medias}
    df_final = pd.DataFrame(data)

    # Salvar o DataFrame em um arquivo CSV (opcional)
    df_final.to_csv(f'{diretorio}/dados_finais_{current_tree}_{current_inst}.csv', index=False)
