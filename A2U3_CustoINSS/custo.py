salario = float(input())

empregador = salario * 0.12

if salario <= 1317.07:
    emp1 = salario * 0.08
    print(f'O valor da contribuição do INSS a ser pago pelo empregador é de R$ {empregador:.2f}')
    print(f'O valor da contribuição do INSS a ser pago pelo empregado é de R$ {emp1:.2f}')
elif 1317.07 < salario <= 2195.12:
    emp2 = salario * 0.09
    print(f'O valor da contribuição do INSS a ser pago pelo empregador é de R$ {empregador:.2f}')
    print(f'O valor da contribuição do INSS a ser pago pelo empregado é de R$ {emp2:.2f}')
elif salario > 2195.12:
    emp3 = salario * 0.11
    print(f'O valor da contribuição do INSS a ser pago pelo empregador é de R$ {empregador:.2f}')
    print(f'O valor da contribuição do INSS a ser pago pelo empregado é de R$ {emp3:.2f}')
