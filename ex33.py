n1 = int(input('Digite um numero 1: '))
n2 = int(input('Digite um numero 2: '))
n3 = int(input('Digite um numero 3: '))

if n1 > n2 and n1 > n3:
    print(f'{n1} é o maior número')
elif n2 > n1 and n2 > n3:
    print(f'{n2} é o maior número')
else:
    print(f'{n3} é o maior número')

if n1 < n2 and n1 < n3:
    print(f'{n1} é o menor número')
elif n2 < n1 and n2 < n3:
    print(f'{n2} é o menor número')
else:
    print(f'{n3} é o menor número')
