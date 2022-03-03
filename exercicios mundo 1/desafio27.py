nome = str(input('Digite seu nome completo:\n')).title()
print(f'Primeiro nome: {nome.split()[0]}')
print(f'Ultimo nome: {nome.split()[-1]}')