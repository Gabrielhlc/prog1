from math import pi
diametro = int(input())
raio = diametro / 2
area = pi * (raio ** 2)
perimetro = 2 * pi * raio

print(f'A: {area:.5f}')
print(f'P: {perimetro:.5f}')
