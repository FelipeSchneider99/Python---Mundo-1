frase = str(input('Digite uma frase: ').strip().upper())
print(f'A letra A aparece {frase.count('A')} vezes'
f'\nA letra A aparece pela primeira vez na posição {frase.find('A')+1}'
f'\nA letra A aparece pela ultima vez na posição {frase.rfind('A')+1}')