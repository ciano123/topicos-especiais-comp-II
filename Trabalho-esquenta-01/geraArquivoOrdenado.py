def gera_arquivo_ordenados(num):
    return list(range(num + 1))

def grupo_linhas(numbers):
    return [numbers[i:i+10] for i in range(0, len(numbers), 10)]

def salva_arquivo(filename, lines):
    with open(filename, 'w') as arquivo:
        for linha in lines:
            arquivo.write(','.join(map(str, linha)) + '\n')

def main(num):
    random_numbers = gera_arquivo_ordenados(num)
    lines = grupo_linhas(random_numbers)
    salva_arquivo(f'{num}.txt', lines)

if __name__ == "__main__":
    lista = [100, 200, 1000, 2000, 5000, 10000, 50000, 100000, 500000, 1000000, 5000000, 10000000, 100000000]

    for i in lista:
        main(num=i)
