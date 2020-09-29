print('Análise da Turma\n===')

num_aprov = int(input('Número de aprovados? '))
num_reprov = int(input('Número de reprovados? '))

print('---')

total = num_aprov + num_reprov

aprovados = (num_aprov * 100) / total
reprovados = (num_reprov * 100) / total 

print(f'Total de alunos na turma: {total}')
print(f'Aprovados: {num_aprov} = {aprovados:.1f}%')
print(f'Reprovados: {num_reprov} = {reprovados:.1f}%')

