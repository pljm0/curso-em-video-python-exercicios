from math import sqrt
co = float(input('Digite a medida do cateto oposto: '))
ca = float(input('Digite a medida do cateto adjacente: '))
print('Para descobrir a medida da hipotenusa utilizamos a formula a²=b²+c²')
print('Onde a² = hipotenusa, b² = cateto oposto e c² = cateto adjacente')
print(f'A formula fica da seguinte forma: \na²={co}²+{ca}² \na²={co**2:.2f}+{ca**2:.2f} \na=√{co**2+ca**2:.2f}')
print(f'a={sqrt(co**2+ca**2):.2f}')
# print(f'Hipotenusa eh: {hypot(co, ca):.2f}cm')
print(f'Com base nisso, podemos concluir que o valor da hipotenusa eh de: a={sqrt(co**2+ca**2):.2f}cm')

# (co**2 + ca**2) ** (1/2) hipotenusa
# math.hypot(co, ca) hipotenusa