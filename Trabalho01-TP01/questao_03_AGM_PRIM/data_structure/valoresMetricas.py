import time
import sys
import tracemalloc  # Para medir o uso de memória
from data_structure.geraRelatorio import gerar_relatorio
from data_structure.gerarGrafico import gerar_grafico_e_salvar

def medir_tempo_memoria(iteracoes, codigo, nomeArquivo, nomeGDiretorio, nomeRDiretorio):
    informacoes_relatorio = []
    # Variaveis para guardar tempo total e memoria
    total_tempo = 0
    total_memoria = 0
    # Inicia a contagem de memoria 
    tracemalloc.start()
    # Executa o loop com o numero de iterações fornecidas pelo usuario
    for _ in range(iteracoes):
        inicio_tempo = time.time()

        codigo()  # Executa o trecho de código fornecido 

        fim_tempo = time.time()
        # Calcula o tempo gasto total
        tempo_gasto = fim_tempo - inicio_tempo
        total_tempo += tempo_gasto
        # Tira um estantaneo de memoria usada até esse momento e calcula a memoria usada
        snapshot = tracemalloc.take_snapshot()
        memoria_usada = sum(stat.size for stat in snapshot.statistics("lineno"))

        total_memoria += memoria_usada
    # Calcula a média de tempo e memoria utilizada
    media_tempo = total_tempo / iteracoes
    media_memoria = total_memoria / iteracoes
    # Captura as informações
    informacoes_relatorio.append(f"Iteracoes: {iteracoes}")
    informacoes_relatorio.append(f"Tempo total: {total_tempo:.5f} segundos")
    informacoes_relatorio.append(f"Memoria total: {total_memoria:.2f} bytes")
    informacoes_relatorio.append(f"Tempo Medio: {media_tempo:.5f} segundos")
    informacoes_relatorio.append(f"Memoria Media: {media_memoria:.2f} bytes")
    # Gera relatorio com as informações capturadas 
    gerar_relatorio(nomeRDiretorio, nomeArquivo, informacoes_relatorio)
    #Gera gráfico e salva no caminho especificado
    gerar_grafico_e_salvar(informacoes_relatorio, nomeArquivo, nomeGDiretorio)
