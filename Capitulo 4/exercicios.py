import numpy as np
import random

# Crie um Array de tamanho 21 com valores linearmente espaçados entre 0 e 1
print("---------- 1 ----------")

array_linear = np.linspace(0, 1, 21)
print(array_linear)

# Crie dois Arrays: um de número pares de 0 até 51 e outro também de número pares de 100 até 50. Em seguida, os concatene e mostre os resultados ordenados
print("\n---------- 2 ----------")

array_pares1 = np.arange(0, 52, 2)
array_pares2 = np.arange(100, 49, -2)

array_concatenado = np.concatenate((array_pares1, array_pares2))

array_ordenado = np.sort(array_concatenado)

print(array_ordenado)

# Ordene os resultados do array resultante da questão anterior em ordem decrescente
print("\n---------- 3 ----------")

array_decrescente = np.sort(array_concatenado)[::-1]

print(array_decrescente)

# Crie uma matriz formada somente por uns de tamanho 3x4. Em seguida, transforme-a em um Array 1-D
print("\n---------- 4 ----------")

matriz_um = np.ones((3, 4))

array_1d = matriz_um.flatten()

print("Matriz 3x4:")
print(matriz_um)

print("\nArray 1-D:")
print(array_1d)

# Crie uma matriz de tamanho qualquer. Extraia seu número de linhas e colunas, multiplique-os, e diga se esta matriz poderia se tornar um vetor com número par ou ímpar de elementos
print("\n---------- 5 ----------")

mtz = np.zeros((random.randint(1,10),random.randint(1,10)))

print("Formato:", mtz.shape)

x = mtz.shape[0]
y = mtz.shape[1]

z = x*y

if z%2 == 0:
    print("Poderia ser um vetor com numero par de elementos")
else:
    print("Poderia ser um vetor com numero impar de elementos")