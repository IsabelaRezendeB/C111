# EXERCÍCIO 1

times = ['Real Madrid', 'Milan', 'Bayern de Munique', 'Barcelona', 'Sao Paulo']

print('3 primeiros colocados:')
print(times[0:3])

print('2 ultimos colocados:')
print(times[3:])

print('Ordem alfabetica:')
print(sorted(times))

print('Posicao de Barcelona:')
i = 0
while i < 5:
    if 'Barcelona' == times[i]:
        print(i + 1)
        break
    i += 1