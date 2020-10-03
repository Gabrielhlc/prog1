n1 = float(input())
n2 = float(input())
n3 = float(input())
faltas = int(input())
media = (n1 + n2 + n3) / 3
if faltas >= 8:
    print('reprovado por faltas')
elif faltas < 8:
    if media < 4:
        print('reprovado por nota')
    elif 4 <= media < 7:
        print('prova final')
    elif media >= 7:
        print('aprovado por media')
