import math
raio = float(input())

diametro = raio * 2
lado =  diametro / math.sqrt(2)
area_circun = math.pi * raio ** 2
area_quad = lado ** 2
diferenca = area_circun - area_quad

print(f'Área não comum: {diferenca:.5f}')
