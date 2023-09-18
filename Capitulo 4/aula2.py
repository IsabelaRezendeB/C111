import numpy as np

# Gerando números aleatórios
np.random.seed(10)
arr = np.random.randint(1, 50, 25)

print(arr)

# Extraindo valores únicos
print(np.unique(arr, return_counts=True))

# Operações linha a linha e coluna a coluna em uma matriz
mtz = np.random.randint(1, 10, 12).reshape([3,4])

print(mtz)
print(mtz.sum(axis=0)) # Retorna vetor com soma dos elementos das colunas
print(mtz.sum(axis=1)) # Retorna vetor com soma dos elementos das linhas
print(mtz.mean(axis=0)[0]) # média da primeira coluna

# Broadcasting
print(mtz/5)
print(mtz*10)

# Condicional
print(mtz[mtz%2==0])
print(mtz[mtz>5])

# NumPy para textos
arr2 = np.array(['Sarah', 'Isabela', 'Lucas', 'Fernanda', 'Gualter'])
result = np.char.find(arr2, 'F')
print(result)
print(arr2[result >= 0])

# Trabalhando com Data Sets
dataset = np.loadtxt('arquivos/space.csv', delimiter=';', dtype=str, encoding='utf-8')
print(dataset[0,:])
