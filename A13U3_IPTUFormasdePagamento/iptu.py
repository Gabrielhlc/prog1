area = float(input())
valor = float(input())
opc = input()

imposto = area * valor
if opc == 'vista':
    desconto = imposto * 0.8
    print(f'Total: R$ {desconto:.2f}')
elif opc == '2x':
    desconto = imposto * 0.9
    parcelas = desconto / 2
    print(f'Total: R$ {desconto:.2f}. Parcelas: R$ {parcelas:.2f}')
else:
    desconto = imposto * 0.95   
    parcelas = desconto / 3
    print(f'Total: R$ {desconto:.2f}. Parcelas: R$ {parcelas:.2f}')
