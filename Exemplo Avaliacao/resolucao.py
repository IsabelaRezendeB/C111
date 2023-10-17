import numpy as np

dataset = np.loadtxt('arquivos/paises.csv', delimiter=';', dtype=str, encoding='utf-8')
#print(dataset[0,:])

# Questão 1 - Faça um slicing no dataset para mostrar apenas o país (Country), região (Region), população (Population) e area (Area (sq. mi.)) dos países contidos nele.

print("\n---------- 1 ----------")
print(dataset[:,0:4])

# Questão 2 - Conte e em seguida mostre quais são as diferentes Regiões do planeta segundo este dataset.

print("\n---------- 2 ----------")
regions = np.unique(dataset[1:,1], return_counts=True)
nomes = regions[0]
num = len(regions[1])
print("Quantidade de regioes:", num)
print("Nomes: ", nomes)

# Questão 3 - Mostre qual a taxa média de alfabetização (Literacy (%)) do planeta segundo este dataset.

print("\n---------- 3 ----------")
percentage = np.mean(dataset[1:,9].astype(float))
print(f"Taxa media de alfabetizacao: {percentage:.2f}%")

# Questão 4 - Conte quantos países são da América do Norte (NORTHERN AMERICA) segundo este dataset

print("\n---------- 4 ----------")
locations = dataset[:, 1]
result = np.char.find(locations, 'NORTHERN AMERICA')
loc_sum = len(locations[result >= 0])
print("Paises da America do Norte: ", loc_sum)

# Questão 5 - Encontre qual país da América do Sul e Caribe (LATIN AMER. & CARIB) possui a maior renda per capita (GDP ($ per capita)).

print("\n---------- 5 ----------")
locations = dataset[1:, 1]
gdp = dataset[1:, 8].astype(float)

result = np.char.find(locations, 'LATIN AMER. & CARIB')
gdp_amr = gdp[result>=0]
indice = np.where(gdp==np.max(gdp_amr))[0][0]

print("Pais: ", dataset[indice+1, 0])
print("Renda per capita: ", np.max(gdp_amr))
