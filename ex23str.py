# import random
#
# num = random.randint(0, 9999)

num = int(input('Digite um numero de 0 a 9999: '))
num_str= str(num)
if 0 <= num <= 9999:
    num_str_formatado = num_str.zfill(4)
    print(f'O numero gerado foi: {num_str_formatado}'
      f'\nUnidade: {num_str_formatado[3]}'
      f'\nDezena: {num_str_formatado[2]}'
      f'\nCentena: {num_str_formatado[1]}'
      f'\nMilhar: {num_str_formatado[0]}')
else:
    print('Numero invalido')