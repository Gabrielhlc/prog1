graus    = int(input())
minutos  = int(input())
segundos = int(input())



minutos_conv = minutos / 60
segundos_conv = segundos / 3600

calculo = graus + minutos_conv + segundos_conv

print(f'graus = {calculo:.4f}')


