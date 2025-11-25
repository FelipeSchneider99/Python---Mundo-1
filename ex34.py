sal = float(input('Qual o seu salario? R$'))

if sal > 1250:
    sal = sal + (sal * 0.10)
    print(f'O valor do seu salario ficou R${sal:.2f}')

else:
    sal = sal + (sal * 0.15)
    print(f'O valor do seu salario ficou R${sal:.2f}')