antes = float(input()) 
depois = float(input()) 

porc_carne = (100 * depois) / antes
porc_agua = 100 - porc_carne

print(f'{porc_agua:.1f}% do peso do produto é de água congelada.')

if porc_agua < 5:
    print('Produto qualis A.')
elif 5 <= porc_agua < 10:
    print('Produto em conformidade.')
else:
    print('Produto não conforme.')
