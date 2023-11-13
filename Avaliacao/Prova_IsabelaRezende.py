import numpy as np

dataset = np.loadtxt('arquivos/shopping_trends.csv', delimiter=',', dtype=str, encoding='utf-8')

print("*** Questao 1 ***")
media_idade = dataset[1:,1].astype(float).mean()
print(f"Media de idade: {media_idade:.2f}")

print("\n*** Questao 2 ***")
gastos = dataset[1:,5].astype(float)
media_gastos = gastos.astype(float).mean()
print(f"Media de gasto: {media_gastos:.2f}")
print("Numero de clientes que gastaram mais que a media:",gastos[gastos.astype(float) > media_gastos].size)

print("\n*** Questao 3 ***")
itens_vendidos = dataset[1:,3]
qnt = np.unique(itens_vendidos, return_counts=True)[1].min()
porcentagem = ( qnt / itens_vendidos.size ) * 100
print(f"Porcentagem de vendas do item menos vendido da loja: {porcentagem:.2f}%")

print("\n*** Questao 4 ***")
desconto = dataset[1:,13]
qnt_desconto = desconto[np.char.find(desconto, "Yes") >= 0].size
porcentagem_desconto = ( qnt_desconto / itens_vendidos.size ) * 100
print(f"Porcentagem de vendas que tiveram desconto: {porcentagem_desconto:.2f}%")

print("\n*** Questao 5 ***")
ds_clothing_summer = dataset[ ( np.char.find(dataset[:,4], "Clothing") >= 0 ) & ( np.char.find(dataset[:,9], "Summer") >= 0 )] # filtrando onde Category = Clothing e onde Season = Summer
index = np.argmax(np.unique(ds_clothing_summer[1:,8], return_counts=True)[1])
cor_pop = np.unique(ds_clothing_summer[1:,8], return_counts=True)[0][index]
print("Cor de roupa mais popular no verao:", cor_pop)