nome = str(input('Digite seu nome completo: ')).strip()

print(f'Seu nome em letras maiusculas: {nome.upper()}')
print(f'Seu nome em letras minusculas: {nome.lower()}')
print(f'Quantidade de letras: {len(nome) - nome.count(' ')}')
print(f'Seu primeiro nome é: {nome.split()[0]} e ele tem {nome.find(' ')} letras')
