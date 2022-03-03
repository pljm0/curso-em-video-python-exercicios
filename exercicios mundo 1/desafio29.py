from random import randint, choice
from string import ascii_uppercase
print(f'{"RADAR ELETRONICO":=^30}')
speed = randint(1, 200)
a1 = str(randint(0, 9))
a2 = str(randint(0, 9))
a3 = str(randint(0, 9))
a4 = str(randint(0, 9))
a5 = choice(ascii_uppercase)
a6 = choice(ascii_uppercase)
a7 = choice(ascii_uppercase)
print(f'Velocidade do veiculo: {speed}km/h')
if speed > 80:
    print('Multa registrada!')
    print(f'Detalhes: \nVelocidade: {speed}km/h')
    print(f'Valor da multa: R${float((speed-80)*7):.2f}')
    print(f'Placa: {a5+a6+a7+a1+a2+a3+a4}')
else:
    print('Velocidade dentro do permitido pela via.')