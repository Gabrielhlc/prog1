orcamento = float(input("Orçamento? R$ "))
num_adultos = int(input("Número de adultos? "))
num_criancas = int(input("Número de crianças? "))
pizza = float(input("Preço da pizza? R$ "))
refrigerante = float(input("Preço do refrigerante? R$ "))
estacionamento = float(input("Preço do estacionamento? R$ "))
ingresso = float(input("Preço do ingresso do cinema? R$ "))
#Ok

alimentacao = pizza + refrigerante #Ok
adultos = num_adultos * ingresso + (2 * num_adultos)#Ok 
criancas = num_criancas * (ingresso / 2) + (2 * num_criancas) #Ok
cinema = adultos + criancas #Ok
total = alimentacao + cinema + estacionamento #Ok
por_pessoa = total / (num_adultos + num_criancas)
saldo = orcamento - total #OK

print("========== Despesas do cinema ==========")
print(f"Alimentacao: R$ {alimentacao:.2f}") #Ok
print(f"Cinema: R$ {cinema:.2f}")
print(f"Custo médio por pessoa: R$ {por_pessoa:.2f}")
print(f"Total: {total:.2f}")
print(f"Saldo após passeio: {saldo:.2f}")

