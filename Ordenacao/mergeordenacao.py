import time
import numpy as np

def merge_sort(arr):
    trocas = 0
    comparacoes = 0

    if len(arr) > 1:
        meio = len(arr) // 2
        metade_esquerda = arr[:meio]
        metade_direita = arr[meio:]

        trocas_esquerda, comparacoes_esquerda = merge_sort(metade_esquerda)
        trocas_direita, comparacoes_direita = merge_sort(metade_direita)

        trocas += trocas_esquerda + trocas_direita
        comparacoes += comparacoes_esquerda + comparacoes_direita

        i = j = k = 0

        while i < len(metade_esquerda) and j < len(metade_direita):
            comparacoes += 1
            if metade_esquerda[i] < metade_direita[j]:
                arr[k] = metade_esquerda[i]
                i += 1
            else:
                arr[k] = metade_direita[j]
                j += 1
            k += 1

        while i < len(metade_esquerda):
            arr[k] = metade_esquerda[i]
            i += 1
            k += 1
            trocas += 1

        while j < len(metade_direita):
            arr[k] = metade_direita[j]
            j += 1
            k += 1
            trocas += 1

    return trocas, comparacoes

def run_experiment(algorithm, size, case_type, repetitions=5):
    np.random.seed(42)  # Para garantir a reprodutibilidade dos resultados

    total_time = 0
    total_swaps = 0
    total_comparisons = 0

    for _ in range(repetitions):
        if case_type == 'Melhor Caso':
            arr = np.arange(size)
        elif case_type == 'Caso Médio':
            arr = np.random.randint(0, size, size).tolist()
        elif case_type == 'Pior Caso':
            arr = np.arange(size, 0, -1)

        start_time = time.time()
        trocas, comparacoes = algorithm(arr.copy())
        end_time = time.time()

        total_time += end_time - start_time
        total_swaps += trocas
        total_comparisons += comparacoes

    tempo_execucao_medio = total_time / repetitions
    trocas_medio = total_swaps / repetitions
    comparacoes_medio = total_comparisons / repetitions

    print(f"Algoritmo: {algorithm.__name__}")
    print(f"Tamanho do array: {size}")
    print(f"Caso: {case_type}")
    print(f"Média do Tempo de Execução: {tempo_execucao_medio:.6f} segundos")
    print(f"Média de Trocas: {trocas_medio}")
    print(f"Média de Comparações: {comparacoes_medio}")
    print("=" * 30)

# Tamanhos de array
tamanhos = [1000, 10000, 100000]

# Tipos de casos
casos = ['Melhor Caso', 'Caso Médio', 'Pior Caso']

# Algoritmos a serem comparados
algoritmo = merge_sort

# Executar experimentos apenas para o Merge Sort
for tamanho in tamanhos:
    for caso in casos:
        run_experiment(algoritmo, tamanho, caso)
