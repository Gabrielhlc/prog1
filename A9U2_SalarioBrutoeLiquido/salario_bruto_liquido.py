nome = input()
horas_extras = float(input())
salario_minimo = float(input())
valor_hora = float(input())

salario_extra = horas_extras * valor_hora
salario_bruto = (4 * salario_minimo) + salario_extra

salario_liquido = salario_bruto * 0.68

print(f'O Salário Bruto de {nome} é de R$ {salario_bruto:.2f}')
print(f'O Salário Líquido de {nome} é de R$ {salario_liquido:.2f}')
