from random import choice
print('Bem-vindo! Nesse programa, o robo Zero ira escolher um numero aleatorio entre 0 e 5, tente adivinhar qual eh!')
print('ZERO: Escolhendo um numero...')
print('ZERO: Numero escolhido!')
input('Pressione enter para continuar')
n1 = int(input('O numero que voce ira escolher sera: \n'))
if n1 > 5:
    print('Por favor, digite apenas um numero entre 0 e 5')
    quit()
rand = choice([0,1,2,3,4,5])
if n1 == rand:
    print('ZERO: PARABENS! Voce acertou!!')
else:
    print('ZERO: Que pena, voce errou.')