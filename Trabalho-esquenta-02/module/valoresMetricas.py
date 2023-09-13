import time
import sys
import tracemalloc  # Para medir o uso de memória
from module.geraRelatorio import gerar_relatorio
from module.gerarGrafico import gerar_grafico_e_salvar

def medir_tempo_memoria(iteracoes, codigo, nomeArquivo, nomeGDiretorio, nomeRDiretorio):
    informacoes_relatorio = []

    total_tempo = 0
    total_memoria = 0

    tracemalloc.start()

    for _ in range(iteracoes):
        inicio_tempo = time.time()

        codigo()  # Executa o trecho de código fornecido

        fim_tempo = time.time()
        tempo_gasto = fim_tempo - inicio_tempo
        total_tempo += tempo_gasto

        snapshot = tracemalloc.take_snapshot()
        memoria_usada = sum(stat.size for stat in snapshot.statistics("lineno"))

        total_memoria += memoria_usada

    media_tempo = total_tempo / iteracoes
    media_memoria = total_memoria / iteracoes

    informacoes_relatorio.append(f"Iteracoes: {iteracoes}")
    informacoes_relatorio.append(f"Tempo total: {total_tempo:.5f} minutos")
    informacoes_relatorio.append(f"Memoria total: {total_memoria:.2f} bytes")
    informacoes_relatorio.append(f"Tempo Medio: {media_tempo:.5f} minutos")
    informacoes_relatorio.append(f"Memoria Media: {media_memoria:.2f} bytes")
    
    gerar_relatorio(nomeRDiretorio, nomeArquivo, informacoes_relatorio)
    #Gera gráfico e salva no caminho especificado
    gerar_grafico_e_salvar(informacoes_relatorio, nomeArquivo, nomeGDiretorio)
