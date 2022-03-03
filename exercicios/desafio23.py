n1 = int(input('Digite um valor entre 0 e 9999:\n'))
str = str(n1).zfill(4)
print(f'Unidade: {str[3]}')
print(f'Dezena: {str[2]}')
print(f'Centena: {str[1]}')
print(f'Milhar: {str[0]}')

# u = n1 // 1 % 10