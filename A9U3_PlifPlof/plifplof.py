n1 = int(input())
n2 = int(input())
n3 = int(input())

soma = n1 + n2 + n3
soma3 = soma % 3
soma5 = soma % 5
if soma3 == 0 and soma5 == 0:
    print('plifplof')
elif soma3 == 0:
    print('plif')
elif soma5 == 0:
    print('plof')
