# EXERCÍCIO 2

loja1 = {'Galaxy S23', 'Redmi Note 11', 'Galaxy Z Flip5', 'Poco M4'}
loja2 = {'Galaxy S23', 'Redmi Note 11', 'Moto g42', 'Moto g22'}

print('Todos os modelos disponiveis (sem repeticao):')
produtos = loja1 | loja2
print(produtos)

print('Modelos disponiveis na loja 1:')
print(loja1)

print('Modelos disponiveis na loja 2:')
print(loja2)