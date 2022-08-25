#Ler nome e duas notas
#Guardar as duas notas em outra lista dentro da lista

import enum
from statistics import median

data = []
ls = []
nota = []
r = ''

while r != 'N':
    ls.append(str(input('Digite o nome: ')))
    nota.append(float(input('Digite a 1° nota: ')))
    nota.append(float(input('Digite a 2° nota: ')))

    #media.append(median(nota))

    ls.append(nota[:])
    ls.append(median(nota))

    data.append(ls[:])
    nota.clear()
    ls.clear()
    r = str(input('Deseja cadastrar mais alunos? S/N ')).upper()

#print(data)



for c,v in enumerate(data):
    print (f'{(c+1):<4}{v[0]:<10}{v[2]:<8.1f}')