import csv
import timeit
import numpy as np

# Carrega os dados em uma lista comum
matrizNativa = []

with open("dados.csv", encoding="utf-8") as arquivo:
    leitor = csv.reader(arquivo)
    next(leitor)

    for idade, nota, frequencia in leitor:
        matrizNativa.append([
            int(idade),
            float(nota),
            float(frequencia)
        ])

# Converte para ndarray
matrizNumpy = np.array(matrizNativa)

# Operações de exemplo
def operacao_nativa():
    return [linha[1] + 0.5 for linha in matrizNativa if linha[1] <= 9.5]

def operacao_numpy():
    return matrizNumpy[:, 1][matrizNumpy[:, 1] <= 9.5] + 0.5

# Benchmark
tempo_nativo = timeit.timeit(operacao_nativa, number=10000)
tempo_numpy = timeit.timeit(operacao_numpy, number=10000)

# Exibição dos resultados
print(f"Tempo (lista nativa): {tempo_nativo:.6f}s")
print(f"Tempo (NumPy):        {tempo_numpy:.6f}s")
print(f"NumPy foi {tempo_nativo / tempo_numpy:.2f}x mais rápido")

