capac = float(input('Capacidade de revestimento? '))
print('\n== Dados do vão a revestir ==')
comp = float(input('Comprimento? '))
larg = float(input('Largura? '))
alt = float(input('Altura? '))

chao = comp * larg
parede = alt * larg 

tudo = chao + (parede * 4)
caixas = tudo / capac
print('\n== Resultados ==')
print(f'Área total a revestir: {tudo:.1f} m2')
print(f'Número de caixas: {caixas:.0f}')
