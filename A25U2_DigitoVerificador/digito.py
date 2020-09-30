n = input()

x1 = int(n[0])
x2 = int(n[1])
x3 = int(n[2])
x4 = int(n[3])
x5 = int(n[4])
calculo1 = x1 + x2 + x3 + x4 + x5
calculo2 = calculo1 % 11

print(f'{n}-{calculo2:02.0f}')

