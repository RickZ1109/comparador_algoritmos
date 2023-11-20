import time
import numpy as np

def quick_sort(arr):
    trocas = 0
    comparacoes = 0

    def partition(arr, low, high):
        nonlocal trocas, comparacoes
        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            comparacoes += 1
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                trocas += 1

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        trocas += 1
        return i + 1

    def quick_sort_iterative(arr, low, high):
        stack = [(low, high)]

        while stack:
            low, high = stack.pop()
            if low < high:
                partition_index = partition(arr, low, high)
                stack.append((low, partition_index - 1))
                stack.append((partition_index + 1, high))

        return trocas, comparacoes

    start_time = time.time()
    trocas, comparacoes = quick_sort_iterative(arr, 0, len(arr) - 1)
    end_time = time.time()

    tempo_execucao = end_time - start_time

    return trocas, comparacoes

def run_experiment(algorithm, size, case_type):
    np.random.seed(42) # Para garantir a reprodutibilidade dos resultados
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
algoritmo = quick_sort

# Executar experimentos apenas para o Quick Sort
for tamanho in tamanhos:
    for caso in casos:
        run_experiment(algoritmo, tamanho, caso)
