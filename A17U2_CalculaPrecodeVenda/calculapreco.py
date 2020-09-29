custo = float(input())
despesas = float(input())
lucro = float(input())
impostos = float(input())
coms = float(input())
descontos = float(input())
encargos = float(input())

perc_despesas = (despesas / 100) * custo
perc_lucro = (lucro / 100) * custo  


preco_venda = (custo + perc_despesas + perc_lucro) * 100 / (100 - impostos - coms - descontos - encargos) 

frac = preco_venda - int(preco_venda)

print(f'Preço de venda é R$ {preco_venda:.2f} (R$ {int(preco_venda):.2f} + R$ {frac:.2f})')
                                                                                                                                                                                                          
                                                                                                
