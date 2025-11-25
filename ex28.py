import random
from time import sleep

num_com = random.randint(0,5)
num_usu = int(input(f'Vou pensar em um numero de 0 a 5. '
                    f'\nTente adivinhar é: '))
print('ANALISANDO...')
sleep(2)
if num_com == num_usu:
    print('Parabens, voce acertou o numero que pensei!!')
    print(f'Pensei no número {num_com}')
elif num_usu <= 5:
    print('Eu ganhei!! Voce errou!!')
    print(f'Pensei no número {num_com}')
else:
    print('Numero invalido')

