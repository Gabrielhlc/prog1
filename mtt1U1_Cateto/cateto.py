import math
a1 = float(input('hipotenusa? '))
cat1 = float(input('cateto? '))

calc1 = (a1 ** 2) - (cat1 ** 2)

cat2 = math.sqrt(calc1)

print(f'hipotenusa: {a1:.2f}\ncateto 1: {cat1:.2f}\ncateto 2: {cat2:.2f}')
