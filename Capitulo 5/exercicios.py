import pandas as pd
import numpy as np

paises = pd.read_csv('arquivos/paises.csv', delimiter=';')

print(" *** Questao 1 *** ")

paises_oceania = paises[paises.Region.str.contains("OCEANIA")]
print("Quantidade de Paises na Oceania: ", len(paises_oceania))
print("Paises: \n", paises_oceania['Country'])

print(" *** Questao 2 *** ")
media = paises['Literacy (%)'].mean()
print(f"Media de gasto: {media:.2f}")

print(" *** Questao 3 *** ")
# Acha a linha que possui maior populacao
linha_pais = paises.loc[paises['Population'].idxmax()]
# Printa a coluna Country dessa linha
print("Pais com maior populacao:", linha_pais['Country'])
print("Regiao:", linha_pais['Region'])
print("Numero de habitantes:", linha_pais['Population'])

print(" *** Questao 4 *** ") # Coastline (coast/area ratio) == 0
paises_no_coast = paises[paises['Coastline (coast/area ratio)'] == 0]
paises_no_coast.to_csv('arquivos/noCoast.csv', sep=';')
print("Arquivo salvo na pasta arquivos")
