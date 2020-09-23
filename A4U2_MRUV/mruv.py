pos_inicial = float(input('Posição inicial? '))
vel_inicial = float(input('Velocidade inicial? '))
tempo = float(input('Tempo? '))
acel = float(input('Aceleração? '))


vel_media = vel_inicial + ((acel * tempo) / 2)
pos_final = pos_inicial + (vel_inicial * tempo) + (acel * (tempo ** 2) / 2)
vel_final = vel_inicial + (acel * tempo)


print('\nDados da questão\n================')

print(f'   Posição inicial: {pos_inicial:.2f} m')
print(f'Velocidade inicial: {vel_inicial:.2f} m/s')
print(f'        Aceleração: {acel:.2f} m/s2')
print(f'             Tempo: {tempo:.2f} s')
print(f'  Velocidade final: {vel_final:.2f} m/s')
print(f'  Velocidade média: {vel_media:.2f} m/s')
print(f'     Posição final: {pos_final:.2f} m')


