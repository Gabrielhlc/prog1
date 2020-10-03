custo_entrada = float(input())
despesas = float(input())
lucro = float(input())
impostos = float(input())
coms = float(input())
descontos = float(input())
encargos = float(input())

perc_depensas = despesas / 100
perc_lucro = lucro / 100
perc_impostos = impostos / 100
perc_coms = coms / 100
perc_descontos = descontos / 100
perc_encargos = encargos / 100

preco_venda = ((custo_entrada + perc_despesas + perc_lucro) * 100) / (100 - perc_impostos - perc_coms + perc_descontos + perc_encargos)) 

frac = preco_venda - int(preco_venda)

print(f'Preço de venda é R$ {preco_venda} (R$ {int(preco_venda:.0f} + R$ {frac:.2f})') 
