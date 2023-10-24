import numpy as np

dataset = np.loadtxt('arquivos/paises.csv', delimiter=';', dtype=str, encoding='utf-8')
#print(dataset[0,:])

# Questão 1 - Faça um slicing no dataset para mostrar apenas o país (Country), região (Region), população (Population) e area (Area (sq. mi.)) dos países contidos nele.

print("\n---------- 1 ----------")
print(dataset[0,:4])

# Questão 2 - Conte e em seguida mostre quais são as diferentes Regiões do planeta segundo este dataset.

print("\n---------- 2 ----------")
regioes = np.unique(dataset[1:,1])
print("Numero de regioes: ", regioes.size)
print("Regioes: ", regioes)

# Questão 3 - Mostre qual a taxa média de alfabetização (Literacy (%)) do planeta segundo este dataset.

print("\n---------- 3 ----------")
alf = dataset[1:,9].astype(float)
print(f"Taxa media de alfabetizacao: {alf.mean():.2f}%")

# Questão 4 - Conte quantos países são da América do Norte (NORTHERN AMERICA) segundo este dataset

print("\n---------- 4 ----------")
regioes = dataset[1:,1]
america = regioes[np.char.find(regioes,"NORTHERN AMERICA") >= 0]
print("Numero de paises da America do Norte: ", america.size)

# Questão 5 - Encontre qual país da América do Sul e Caribe (LATIN AMER. & CARIB) possui a maior renda per capita (GDP ($ per capita)).

print("\n---------- 5 ----------")
renda = dataset[1:,8].astype(int)
renda_max = renda[np.char.find(regioes,"LATIN AMER. & CARIB") >= 0].max()
lista_renda = list(renda)
print("Pais: ", dataset[:,0][lista_renda.index(renda_max) + 1], "\nRenda: ", renda_max)