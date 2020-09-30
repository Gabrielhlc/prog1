tweet = int(input())

paginas= tweet // 400
porc = (tweet % 400) * 100 / tweet

print(f'Serão necessárias {paginas} página(s) para visualizar os tweets.\n{porc:.1f}% dos tweets serão perdidos.') 

