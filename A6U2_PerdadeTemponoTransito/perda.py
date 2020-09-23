n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())


soma = n1 + n2 + n3 + n4 + n5
media = soma / 5 
sem_prod = soma * 100 / 7200
house = soma / 50

print(f'Você perdeu {soma} min na semana (média de {media:.1f} min por dia).\nIsso significa {sem_prod:.2f}% da sua semana produtiva.\nDaria para assistir {int(house)} episódio(s) de House.')

