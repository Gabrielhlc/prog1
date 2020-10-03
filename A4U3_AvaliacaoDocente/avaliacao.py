n = int(input())
x1 = float(input())
x2 = float(input())
x3 = float(input())
x4 = float(input())
if n < 4:
    print('Promoção indeferida. Número de semestres insuficiente.')
else:
    if x1 < 320 or x2 < 100 or x3 < 20:
        print('Promoção indeferida. Pontuação mínima não alcançada.')
    else:
        media = (x1 + x2 + x3 + x4) / 4
        if media < 140:
            print('Promoção indeferida. Média insuficiente.')
        else:
            print('Promoção deferida. Parabéns!')
