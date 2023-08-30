# EXERCÍCIO 3

nome = input('Entre com o nome: ')
media = input('Entre com a media: ')

aluno = {'Nome':nome, 'Media':int(media)}

if aluno['Media'] >= 60:
    aluno['Situacao'] = 'AP'
else:
    aluno['Situacao'] = 'RP'

print(aluno)