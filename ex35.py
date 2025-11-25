print('TRIANGULO')

reta_a = int(input('Digite o comprimento da reta A: '))
reta_b = int(input('Digite o comprimento da reta B: '))
reta_c = int(input('Digite o comprimento da reta C: '))

if reta_a < 0 or reta_b < 0 or reta_c < 0:
    print('O comprimento deve ser positivo')

elif reta_a + reta_b > reta_c and reta_b + reta_c > reta_a and reta_a + reta_c > reta_b:
    print(f'As medidas {reta_a}, {reta_b}, {reta_c} formam um triangulo!')

else:
    print(f'As medidas não formam um triangulo!')
