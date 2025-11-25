vel = float(input('Qual a velocidade do carro em Km/h? '))
multa = (vel - 80) * 7
if vel > 80:
    print(f'A velocidade maxima permitida é 80Km/h, você estava a {vel:.0f}Km/h.'
          f'\nVocê foi multado!')
    print(f'O valor da multa ficou R${multa:.2f}.')
else:
    print('Voce esta dentro do limite da via!')