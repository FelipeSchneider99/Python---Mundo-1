dist = float(input('Digite a distancia da viagem em Km: '))
if dist <= 200:
    print(f'O valor da passagem ficou R${dist*0.5:.2f}')
else:
    print(f'O valor da passagem ficou R${dist*0.45:.2f}')