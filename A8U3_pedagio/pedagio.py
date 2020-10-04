veiculo = input()
if veiculo == 'Motocicleta':
    print('Valor a pagar: R$ 5.70.')
elif veiculo == 'Automóvel utilitário':
    print('Valor a pagar: R$ 11.40.')
elif veiculo == 'Caminhão':
    eixos = int(input())
    print(f'Valor a pagar: R$ {9.60 * eixos:.2f}.')
elif veiculo == 'Ônibus':
    eixos = int(input())
    print(f'Valor a pagar: R$ {11.40 * eixos:.2f}.')
else:
    print('Veículo não cadastrado.')
