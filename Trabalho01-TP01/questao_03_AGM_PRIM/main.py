import os
from data_structure.algoritmo_PAGM_AB import Prim_AB
from data_structure.algoritmo_PAGM_AVL import Prim_AVL
from data_structure.constroiGrafo import constroi_grafo_de_arquivo
from data_structure.valoresMetricas import medir_tempo_memoria
from data_structure.combina_resultados import combinar_csv
from data_structure.gera_dados_finais import gera_dados_finais


### VARIAVEIS UTILIZADAS ##
# Variavel nome da instancia corrente
current_inst = 'ALUT'
current_tree = 'avl'
# Guarda caminho para geração do gráfico
grafic_file = f"./files/graphics/arvore_{current_tree}/{current_inst}/"
# Guarda caminho para geração de resultados
result_file = f"./files/results/arvore_{current_tree}/{current_inst}/"
# Guarda caminho das instancias utilizadas
diretorio = f"./files/instances/{current_inst}"
# Guarda caminho a lista de arquivos dentro do diretorio das instancias corrente
arquivos = os.listdir(diretorio)

# Inicia a iteração em todos os arquivos
for arquivo in arquivos:
    print(arquivo)
# Inicio analise

    filename = f"{diretorio}/{arquivo}"
    graph = constroi_grafo_de_arquivo(filename)
    # Seta a raiz 
    root = '1'
    
    nome_arquivo = f'Algoritmo_Prim_AB_file_{arquivo}'
    
    def use_algoritmo():
        
        # print("Árvore geradora mínima: Prim AVL")
        # arvore_geradora_minima, total_pesos = Prim_AVL(graph)
        
        print("Árvore Geradora Mínima: Algoritmo Prim AB")
        arvore_geradora_minima, total_pesos, pesos = Prim_AB(graph, root)
        
        # for edge in arvore_geradora_minima:
        #     print(edge, "-", pesos[edge])

        print(f"Peso Total da Árvore Geradora Mínima: {total_pesos}")
        
    medir_tempo_memoria(10, use_algoritmo, nome_arquivo, grafic_file, result_file)

# Combina os resultados em um arquivo results.csv
combinar_csv(result_file, current_inst)
# Gera dataframe com formatação em tabelas com dados principais
gera_dados_finais(result_file, current_inst, current_tree)