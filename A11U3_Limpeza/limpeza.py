servico = int(input())

if servico == 1:
    tamanho = float(input())
    x1 = tamanho * 80 
    print(f'R$ {x1:.0f},00')
    if x1 >= 200:
        print('Brinde!')
elif servico == 2:
    tamanho = float(input())
    x1 = tamanho * 50
    print(f'R$ {x1:.0f},00')
    if x1 >= 200:
        print('Brinde!')
else:
    print('R$ 50,00')
