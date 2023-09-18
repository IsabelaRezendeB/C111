import numpy as np

# Crie um array de floats com 10 elementos positivos e negativos entre 0 e 1. Em seguida, multiplique seus valores por 100 e crie um novo vetor apenas com a parte inteira destes números (use seed(5)).
print("---------- 1 ----------")

np.random.seed(5)
arr = np.random.randn(10)
arr = arr * 100
integer_array = arr.astype(int)
print(integer_array)

# Crie uma matriz de tamanho 4x4 formada por números aleatórios inteiros entre 1 e 50 (use seed(10)).
print("\n---------- 2 ----------")

np.random.seed(10)
mtz = np.random.randint(1, 50, 16).reshape([4,4])
print(mtz)

# Mostre o resultado da média de cada linha e cada coluna da matriz gerada pela questão 2, e em seguida, apresente o maior valor das médias para as linhas e também para as colunas.
print("\n---------- 3 ----------")

print("Medias por linha: ", mtz.mean(axis=1))
print("Medias por coluna: ", mtz.mean(axis=0))
print("Maior media por linha: ", max(mtz.mean(axis=1)))
print("Maior media por coluna: ", max(mtz.mean(axis=0)))

# Baseado na matriz gerada na questão 2, mostre a quantidade de aparições de cada um dos números na mesma. Em seguida, mostre apenas os números que aparecem 2 vezes.
print("\n---------- 4 ----------")

print("Quantidade de aparicao por numero: ", np.unique(mtz, return_counts=True))
mtz_cond = np.unique(mtz, return_counts=True)[0]
print("Numeros que aparecem 2 vezes: ", mtz_cond[np.unique(mtz, return_counts=True)[1] == 2])