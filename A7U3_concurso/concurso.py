c1_n1 = float(input())
c1_n2 = float(input())
c1_n3 = float(input())
c1_age = int(input())
c2_n1 = float(input())
c2_n2 = float(input())
c2_n3 = float(input())
c2_age = int(input())

c1_media = (c1_n1 * 0.3) + (c1_n2 * 0.4) + (c1_n3 * 0.3) 
c2_media = (c2_n1 * 0.3) + (c2_n2 * 0.4) + (c2_n3 * 0.3)

if c1_media > c2_media:
    print(f'O primeiro candidato foi aprovado com média {c1_media:.1f}.')
elif c2_media > c1_media:
    print(f'O segundo candidato foi aprovado com média {c2_media:.1f}.')
elif c1_media == c2_media:
    if c1_age > c2_age:
        print(f'O primeiro candidato foi aprovado com média {c1_media:.1f}.')
    elif c2_age > c1_age:
        print(f'O segundo candidato foi aprovado com média {c2_media:.1f}.')
    elif c1_media == c2_media and c1_age == c2_age:
        print('Empate.')
    else:
        print(f'O segundo candidato foi aprovado com media {c2_media:.1f}.')
