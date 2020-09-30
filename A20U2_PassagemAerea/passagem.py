distancia = float(input())
aliquota = float(input())

valor = (distancia * aliquota) + 51

vista = valor * 0.75

total6 = valor * 0.95
parcelas6 = total6 / 6

parcelas10 = valor / 10
print(f'Valor da passagem: R$ {valor:.2f}\n')
print('Pagamento:')
print(f'1. À vista. R$ {vista:.2f}')
print(f'2. Em 6 parcelas. Total: R$ {total6:.2f}\n   6 x R$ {parcelas6:.2f}')
print(f'3. Em 10 parcelas. Total: R$ {valor:.2f}\n   10 x R$ {parcelas10:.2f}')

