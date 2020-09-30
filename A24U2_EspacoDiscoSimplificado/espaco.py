nome1 = input()
espaco1 = float(input())
nome2 = input()
espaco2 = float(input())
nome3 = input()
espaco3 = float(input())



div1 = espaco1 / 1048576
div2 = espaco2 / 1048576
div3 = espaco3 / 1048576


espaco1 = div1 + div2 + div3
espaco_medio = espaco1 / 3

print('SPLab - Espaço utilizado pelos usuários\n---------------------------------------------')
print('Nr., Usuário, Espaço Utilizado\n')

print(f'1, {nome1}, {div1:.2f} MB\n2, {nome2}, {div2:.2f} MB\n3, {nome3}, {div3:.2f} MB\n')
print(f'Espaço total ocupado: {espaco1:.2f} MB\nEspaço médio ocupado: {espaco_medio:.2f} MB')
