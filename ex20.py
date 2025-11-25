# import random
# alunos = ['Joao', 'Fernando', 'Maria', 'Roberta']
# random.shuffle(alunos)
###-----------The join() method takes all the items in an iterable (like a list) and joins them into one string.
###-----------You can specify a separator to be used between each item.
# ordem= ', '.join(alunos)
# print(f'A ordem de apresentação será: {ordem}')

from random import shuffle
n1 = str(input('Nome do primeiro aluno: '))
n2 = str(input('Nome do segundo aluno: '))
n3 = str(input('Nome do terceiro aluno: '))
n4 = str(input('Nome do quarto aluno: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
ordem = ', '.join(lista)
print(f'A ordem de apresentação será: {ordem}')