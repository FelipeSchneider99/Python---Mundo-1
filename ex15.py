print('Aluguel de carros:')
km = float(input('Quantos kms foram percorridos? '))
dias = int(input('Quantos dias alugados? '))
print('Total a pagar é R${:.2f}'.format((dias*60) + (km* 0.15)))
