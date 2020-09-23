morangos = int(input())


caixas = morangos // 400
porc = (morangos % 400) * 100 / morangos 
print(f'Serão necessárias {caixas:.0f} caixa(s) para embalar os morangos.\n{porc:.1f}% dos morangos serão perdidos.')




#if morangos  <= 400:
 #   caixas = 1
  #  porc = 0
#else:
   # caixas = morangos / 400
  #  porc = (morangos % 400) * 100 / morangos 
