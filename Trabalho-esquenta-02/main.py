from module.tratarArquivo import ler_e_retornar_array
from module.valoresMetricas import medir_tempo_memoria
from module.maiorValor1 import maiorValor1
from module.maiorValor2 import maiorValor2

# from module.valoresMetricas import gerar_relatorio


#, 2000, 5000,10000,50000, 100000,500000,1000000,5000000,10000000,100000000
# Variaveis para diretorios
g_maiorValor1 = './files/graficos/maior_valor1/'
g_maiorValor2 = './files/graficos/maior_valor2/'

r_maiorValor1 = './files/results/maior_valor1/'
r_maiorValor2 = './files/results/maior_valor2/'

# Inicio analise
instancia = '5000'
# nome_arquivo = f'Busca_MaiorValor1-Instancia{instancia}_desordenados'
nome_arquivo = f'Tempo_MaiorValor2-Instancia{instancia}_desordenados'
arquivo_current = f'./files/desordenados/{instancia}.txt'

vetor_numeros = ler_e_retornar_array(arquivo_current)
def use_algoritmo():
    # print(f"Busca Quadrática para instancia de {instance}\n")
    # maiorValor1(vetor_numeros, len(vetor_numeros)-1)
    maiorValor2(vetor_numeros, 0, len(vetor_numeros) - 1)
    # print(f'maior = {result}')
    
medir_tempo_memoria(10, use_algoritmo, nome_arquivo, g_maiorValor2, r_maiorValor2)