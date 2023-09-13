import random

def desordenar_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()

        random.shuffle(linhas)  # Desordena as linhas

        with open(nome_arquivo, 'w') as arquivo:
            arquivo.writelines(linhas)

        print(f"Dados desordenados no arquivo '{nome_arquivo}'.")
    except FileNotFoundError:
        print(f"O arquivo '{nome_arquivo}' não foi encontrado.")