from random import sample
nome1 = str(input('Digite o nome do primeiro aluno do trabalho: '))
nome2 = str(input('Digite o nome do segundo aluno do trabalho: '))
nome3 = str(input('Digite o nome do terceiro aluno do trabalho: '))
nome4 = str(input('Digite o nome do quarto aluno do trabalho: '))
alunos = [nome1, nome2, nome3, nome4]
# shuffle(alunos)
print(f'A ordem dos alunos para a apresentacao do trabalho sera da seguinte forma: ', end=' ')
print(f'{sample(alunos, 4)}')
