quant_mtp = int(input())
if quant_mtp == 1:
    n1 = float(input())
elif quant_mtp == 2: 
    n1 = float(input())
    n2 = float(input())
elif quant_mtp == 3:
    n1 = float(input())
    n2 = float(input())
    n3 = float(input())
elif quant_mtp == 4:
    n1 = float(input())
    n2 = float(input())
    n3 = float(input())
    n4 = float(input())

if quant_mtp < 2:
    print(n1)
    print('Aluno ainda não aprovado na unidade')
elif quant_mtp == 2:
    media2 = (n1 + n2) / 2
    print(media2)
    if media2 < 6:
        print('Aluno ainda não aprovado na unidade')
    else:
        print('Aluno aprovado na unidade')
elif quant_mtp == 3:
    media3 = ((n1 + n2 + n3) / 3) - 0.5
    print(media3)
    if media3 < 6:
        print('Aluno ainda não aprovado na unidade')
    else:
        print('Aluno aprovado na unidade')
elif quant_mtp == 4:
    media4 = ((n1 + n2 + n3 + n4) / 4) - 0.5
    print(media4)
    if media4 < 6:
        print('Aluno ainda não aprovado na unidade')
    else:
        print('Aluno aprovado na unidade')


