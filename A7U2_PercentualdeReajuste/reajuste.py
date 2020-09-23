atual = float(input('Valor atual? '))
novo  = float(input('Novo valor? '))

reajuste = ((novo * 100) / atual) - 100

print(f'Reajuste de {reajuste:.1f}%')
