frase = str(input('Digite uma frase qualquer:\n')).strip().lower()
print(f'Quantas vezes aparece a letra "a": {frase.count("a")}')
print(f'Em que posicao ela aparece a primeira vez: {frase.find("a")+1}')
print(f'Em que posicao ela aparece a ultima vez: {frase.rfind("a")+1}')