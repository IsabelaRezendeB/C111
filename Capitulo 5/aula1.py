import pandas as pd
import numpy as np

"""
# 1D -> Series
# Exige que passemos chave e valor de cada elemento
dic = {'a': 10, 'b': 20, 'c': 30}
series1 = pd.Series(dic)
print(series1)
# Lendo elemento por index
print(series1['a'])
# Lendo múltiplos elementos por index
print(series1[['a','c']])
# Alta compatibilidade entre pandas e numpy
print("Media:", np.mean(series1))
# Usando notação do numpy no pandas
print(series1[1:])
# Condicionais
print(series1[series1 > series1.mean()])
"""

# 2D+ -> DataFrames
# Similar a excel
np.random.seed(10)
df = pd.DataFrame(index=['A', 'B', 'C', 'D', 'E'], # índices das linhas
                  columns=['W', 'X', 'Y', 'Z'], # índices das colunas
                  data=np.random.randint(1, 50, [5,4])) # números aleatórios entre 1 e 50 em formato 5 linhas por 4 colunas
print(df)
# Acessando um único elemento
print(df['Y']['C']) # primeiro coluna, segundo linha
# Acessando uma coluna
print(df['X'])
# Acessando múltiplas colunas
print(df[['X', 'Z']])
# Slicing com loc (usa index pd) e iloc (usa index np)
df2 = df.loc[['A', 'B'], ['X', 'Y', 'Z']]
print(df2)
df3 = df.iloc[:2, 1:]
print(df3)
# Importando DataSet
paises = pd.read_csv('arquivos/paises.csv', delimiter=';')
# Visualisando as colunas
print(paises.columns)
