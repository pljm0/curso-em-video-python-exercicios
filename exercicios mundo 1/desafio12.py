p = float(input('Digite o preco do produto: R$'))
print(f'O preco do produto com 5% de desconto passa a ser: R${p-(p*5/100):.2f}')
print(f'O produto a vista com 10% de desconto: R${p-(p*10/100):.2f}')
print(f'O produto parcelado com 15% de aumento: R${p+(p*15/100):.2f}')