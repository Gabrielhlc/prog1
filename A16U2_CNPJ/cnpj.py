cnpj = input()

x1 = float(cnpj[0])
x2 = float(cnpj[1])
x3 = float(cnpj[3]) 
x4 = float(cnpj[4])
x5 = float(cnpj[5])
x6 = float(cnpj[7])
x7 = float(cnpj[8])
x8 = float(cnpj[9])

proc = 1 + x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8

print(f'{x1:.0f}{x2:.0f}.{x3:.0f}{x4:.0f}{x5:.0f}.{x6:.0f}{x7:.0f}{x8:.0f}/0001-{proc:02.0f}')
