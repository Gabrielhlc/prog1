import math
n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())
n6 = int(input())

d1 = math.sqrt((n1 - n3)**2 + (n2 - n4)**2) 
d2 = math.sqrt((n1 - n5)**2 + (n2 - n6)**2)
d3 = math.sqrt((n3 - n5)**2 + (n4 - n6)**2)

perimetro = d1 + d2 + d3

print(f'O perímetro é de {perimetro:.2f}')
