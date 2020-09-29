# coding: utf-8
# Eleição na ADUF

abstencao = int(input())
favor = int(input())
contra = int(input())

total = abstencao + favor + contra

porc_abs = (abstencao * 100) / total
porc_favor = (favor * 100) / total 
porc_contra = (contra * 100) / total

print('Resultado da Votação\n')
print(f'{abstencao} abstenções ({porc_abs:.2f}%)')
print(f'{favor} a favor ({porc_favor:.2f}%)')
print(f'{contra} contra ({porc_contra:.2f}%)')

