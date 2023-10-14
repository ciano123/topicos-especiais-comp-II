from module.buscaBinaria import busca_binaria
from module.tratarArquivo import ler_e_retornar_array
from module.valoresMetricas import medir_tempo_memoria
from module.buscaQuadratica import busca_quadratica
from module.buscaCubica import busca_cubica
from module.buscaSequencial import busca_sequencial_I
from module.buscaSequencial import busca_sequencial_II
from module.buscaTernaria import busca_ternaria
from module.desordenaArquivo import desordenar_arquivo
# from module.valoresMetricas import gerar_relatorio


#, 2000, 5000,10000,50000, 100000,500000,1000000,5000000,10000000,100000000
# Variaveis para diretorios
g_binaria = './files/graficos/busca_binaria/'
g_cubica = './files/graficos/busca_cubica/'
g_quadratica = './files/graficos/busca_quadratica/'
g_sequencial_1 = './files/graficos/busca_sequencial_1/'
g_sequencial_2 = './files/graficos/busca_sequencial_2/'
g_ternaia = './files/graficos/busca_ternaria/'

r_binaria = './files/results/busca_binaria/'
r_cubica = './files/results/busca_cubica/'
r_quadratica = './files/results/busca_quadratica/'
r_sequencial_1 = './files/results/busca_sequencial_1/'
r_sequencial_2 = './files/results/busca_sequencial_2/'
r_ternaia = './files/results/busca_ternaria/'

# Inicio analise
instancia = '2000'
nome_arquivo = f'Busca_Quadratica-Instancia{instancia}_desordenados'
arquivo_current = f'./files/desordenados/{instancia}.txt'

vetor_numeros = ler_e_retornar_array(arquivo_current)
def use_algoritmo():
    # print(f"Pesquisa Binária para instancia de {i}\n")
    # busca_binaria(0,vetor_numeros[-1], vetor_numeros, 76)
    # print(f"Busca Quadrática para instancia de {instance}\n")
    busca_quadratica(vetor_numeros, 1855)
    # print(f"Busca Cúbica para instancia de {instance}\n")
    # busca_cubica(vetor_numeros, 1468)
    # print(f"Busca Sequencial para instancia de {instance}\n")
    # busca_sequencial_I(vetor_numeros, 50)
    # print(f"Busca Sequencial II para instancia de {instance}\n")
    # busca_sequencial_II(vetor_numeros, 68)
    # print(f"Busca Ternaria para instancia de {instance}\n")
    # busca_ternaria(vetor_numeros, 3446)
# desordenar_arquivo(arquivo_current)
medir_tempo_memoria(30, use_algoritmo, nome_arquivo, g_quadratica, r_quadratica)