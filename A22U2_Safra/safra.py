quant_soja = int(input())
clientes_atac = int(input())
clientes_var = int(input())


quant_soja_client_atac = quant_soja // clientes_atac
quant_soja_var = quant_soja - (quant_soja_client_atac * clientes_atac)

quant_soja_client_var = quant_soja_var / clientes_var

print(f'Clientes no atacado = {quant_soja_client_atac}kg cada.\nClientes no varejo = {quant_soja_client_var:.2f}kg cada.')

