capacidade_total = float(input('capacidade? '))
percentual_atual = float(input('percentual hoje? '))
consumo_diario   = float(input('gasto diário? '))


volume_atual = capacidade_total * (percentual_atual / 100)

dias_restantes = volume_atual // consumo_diario

print(f'volume: {volume_atual:.2f}\ndias restantes: {dias_restantes:.0f}')
