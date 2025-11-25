nome = str(input('Digite seu nome completo: ')).strip()
nome = nome.split()
print(f'Primeiro nome: {nome[0]}'
      f'\nUltimo nome: {nome[-1]}')