grau = float(input())
voltas = grau // 360 
if grau > 360:
    x = grau - (360 * voltas)
    if 0 < x < 90:
        print('Quadrante 1')
    elif 90 < x < 180:
        print('Quadrante 2')
    elif 180 < x < 270:
        print('Quadrante 3')
    elif 270 < x < 360:
        print('Quadrante 4')
    elif x == 0 or x == 90 or x == 180 or x == 270 or x == 360:
        print('Sobre eixos')
else:
    if 0 < grau < 90:
        print('Quadrante 1')
    elif 90 < grau < 180:
        print('Quadrante 2')
    elif 180 < grau < 270:
        print('Quadrante 3')
    elif 270 < grau < 360:
        print('Quadrante 4')
    elif grau == 0 or grau == 90 or grau == 180 or grau == 270 or grau == 360:
        print('Sobre eixos')



   
