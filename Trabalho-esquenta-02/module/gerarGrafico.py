import matplotlib.pyplot as plt

def gerar_grafico_e_salvar(informacoes_relatorio, nomeArquivo, nomeGDiretorio):
    iteracoes = int(informacoes_relatorio[0].split(": ")[1])
    total_tempo = float(informacoes_relatorio[1].split(": ")[1].split()[0])
    total_memoria = float(informacoes_relatorio[2].split(": ")[1].split()[0])
    media_tempo = float(informacoes_relatorio[3].split(": ")[1].split()[0])
    media_memoria = float(informacoes_relatorio[4].split(": ")[1].split()[0])
    #Convertendo valores
    total_tempo = round(float(total_tempo), 5)
    media_tempo = round(float(media_tempo), 5)
    total_memoria = round(float(total_memoria), 2)
    media_memoria = round(float(media_memoria), 2)

    # labels = ['Total Tempo', 'Total Memória', 'Média Tempo', 'Média Memória']
    # valores = [total_tempo, total_memoria, media_tempo, media_memoria]

    labels = ['Total Tempo',  'Média Tempo']
    valores = [total_tempo, media_tempo]
    print("---Valores capturados Grafico------")
    print(f'Iteracoes: {iteracoes}')
    print(f'Total tempo: {total_tempo}')
    print(f'Total memoria: {total_memoria}')
    print(f'Media tempo: {media_tempo}')
    print(f'Media memoria: {media_memoria}')
    plt.plot(labels, valores)
    plt.ylabel('Valores em bytes')
    plt.title(f'Gráfico - {nomeArquivo}')
    
    # Salvar o gráfico como imagem
    nome_arquivo_grafico = f'{nomeArquivo}.png'
    caminho_arquivo_grafico = f'{nomeGDiretorio}{nome_arquivo_grafico}'
    plt.savefig(caminho_arquivo_grafico)
    
    # plt.show()
    print(f"Gráfico gerado e salvo em '{caminho_arquivo_grafico}'.")