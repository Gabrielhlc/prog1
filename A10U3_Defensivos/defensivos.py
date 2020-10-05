produto = input()
hec = float(input())

if produto == 'Fungicida':
   dose = 1
   volume = 50
   preco = 320

elif produto == 'Herbicida':
    dose = 0.3
    volume = 1
    preco = 100
elif produto == 'Inseticida':
    dose = 2.5
    volume = 30
    preco = 400
    
litros = hec * dose
if litros % volume > 0:
    unidade = litros // volume + 1
else:
    unidade = litros // volume 

custo = preco * unidade

print(f'{unidade:.0f} {produto}(s). {custo:.2f} reais.')
