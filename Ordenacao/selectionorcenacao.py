import time
import numpy as np

def selection_sort(arr):
    trocas = 0
    comparacoes = 0

    for i in range(len(arr)):
        min_index = i

        for j in range(i + 1, len(arr)):
            comparacoes += 1
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]
        trocas += 1

    return trocas, comparacoes

def run_experiment(algorithm, size, case_type):
    np.random.seed(42)  # Para garantir a reprodutibilidade dos resultados
    if case_type == 'Melhor Caso':
        arr = np.arange(size)
    elif case_type == 'Caso Médio':
        arr = np.random.randint(0, size, size)
    elif case_type == 'Pior Caso':
        arr = np.arange(size, 0, -1)

    start_time = time.time()
    trocas, comparacoes = algorithm(arr.copy())
    end_time = time.time()

    tempo_execucao = end_time - start_time

    print(f"Algoritmo: {algorithm.__name__}")
    print(f"Tamanho do array: {size}")
    print(f"Caso: {case_type}")
    print(f"Tempo de Execução: {tempo_execucao:.6f} segundos")
    print(f"Quantidade de Trocas: {trocas}")
    print(f"Quantidade de Comparações: {comparacoes}")
    print("=" * 30)

# Tamanhos de array
tamanhos = [1000, 10000, 100000]

# Tipos de casos
casos = ['Melhor Caso', 'Caso Médio', 'Pior Caso']

# Algoritmos a serem comparados
algoritmo = selection_sort

# Executar experimentos apenas para o Selection Sort
for tamanho in tamanhos:
    for caso in casos:
        run_experiment(algoritmo, tamanho, caso)
