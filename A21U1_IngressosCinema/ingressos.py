adultos = int(input())
criancas = int(input())
ingresso = float(input())

inteira = adultos * ingresso 
meia = (criancas * ingresso) / 2
total = inteira + meia

print(f'Total: R$ {total:.2f}')

