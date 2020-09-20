potencia = int(input())
tempo = float(input())

potencia /= 1000
tempo /= 60
calculo = potencia * tempo

print(f'{calculo:.1f} kWh')


