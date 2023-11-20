import timeit
import numpy as np

def shell_sort(arr):
    trocas = 0
    comparacoes = 0

    def sort(arr):
        nonlocal trocas, comparacoes
        n = len(arr)
        gap = n // 2

        while gap > 0:
            for i in range(gap, n):
                trocas += 1
                temp = arr[i]
                j = i

                while j >= gap and arr[j - gap] > temp:
                    comparacoes += 1
                    arr[j] = arr[j - gap]
                    j -= gap

                arr[j] = temp

            gap //= 2

    # Usando timeit para medir o tempo de execução
    tempo_execucao = timeit.timeit(lambda: sort(arr.copy()), number=10)

    return trocas, comparacoes, tempo_execucao

def run_experiment(algorithm, size, case_type):
    np.random.seed(42) # Para garantir a reprodutibilidade dos resultados
    if case_type == 'Melhor Caso':
        arr = np.arange(size)
    elif case_type == 'Caso Médio':
        arr = np.random.randint(0, size, size)
    elif case_type == 'Pior Caso':
        arr = np.arange(size, 0, -1)

    trocas, comparacoes, tempo_execucao = algorithm(arr.copy())

    print(f"Algoritmo: {algorithm.__name__}")
    print(f"Tamanho do array: {size}")
    print(f"Caso: {case_type}")
    print(f"Tempo de Execução (média de 10 execuções): {tempo_execucao:.6f} segundos")
    print(f"Quantidade de Trocas: {trocas}")
    print(f"Quantidade de Comparações: {comparacoes}")
    print("=" * 30)

# Tamanhos de array
tamanhos = [1000, 10000, 100000]

# Tipos de casos
casos = ['Melhor Caso', 'Caso Médio', 'Pior Caso']

# Algoritmos a serem comparados
algoritmo_shell_sort = shell_sort

# Executar experimentos apenas para o Shell Sort
for tamanho in tamanhos:
    for caso in casos:
        run_experiment(algoritmo_shell_sort, tamanho, caso)
