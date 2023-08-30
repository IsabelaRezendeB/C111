# DICIONARIOS

# Basicamente um json

dados = {'Nome':'Goku', 'Idade':42, 'Sexo':'M'}

# Inserção
dados['Cabelo'] = 'Castanho'

# Remoção
del dados['Sexo']

# Alteração
dados['Nome'] = 'Freeza'

# Exibição
print(dados['Idade'])
print(dados)


# COLECOES DENTRO DE COLECOES
dados = {'Nome':'Goku', 'Idade':42, 'Sexo':'M'}
dados2 = {'Nome':'Gohan', 'Idade':28, 'Sexo':'M'}

# Colocando os dois dicionarios dentro de uma lista
personagens = [dados,dados2]

# Como acessar a idade do gohan
print(personagens[1]['Idade'])
print(personagens)