home = ' Painel do Cidadao '
print(f'{home:=^56}\n')
nome = str(input('Informe seu nome completo:\n')).strip()
print(f'Bem-vindo {nome}\n ')
print(f'Nome com todas as letras maiusculas: {nome.upper()}')
print(f'Nome com todas as letras minusculas: {nome.lower()}')
print(f'Quantas letras tem ao todo sem considerar espacos: {len(nome)-nome.count(" ")}')
print(f'Quantas letras tem o primeiro nome: {len(nome.split()[0])}')