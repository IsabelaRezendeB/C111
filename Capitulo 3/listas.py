# LISTAS

# Guarda seus elementos dentro []
# Mutável

nomes = ['Goku', 'Vegeta', 'Trunks', 'Gohan']

# Inserção
nomes.append('Bulma')
nomes.insert(0, 'Kuririn')
print(nomes)

# Alteração
nomes[0] = 'Picolo'
print(nomes)

# Remoção
del nomes[0]
nomes.pop(1)  # Usa um índice
nomes.remove('Trunks')  # Passa um valor
print(nomes)