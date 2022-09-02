from statistics import mean, median
import statistics

medma = []
med = []
mul = []
data = {}
lis = []
r = ''
while r != 'N':
    data['nome'] = str(input('Digite seu nome: '))
    while data['nome'] in str:
        data['nome'] = str(input('Digite seu nome: '))

    data['sexo'] = str(input('Digite seu sexo M/F: ')).upper()

    if data['sexo'] == 'F':
        mul.append(data['nome'])

    data['idade'] = int(input('Digite sua idade: '))
    med.append(data['idade'])

    r = str(input('Deseja continuar? S/N: ')).upper()
    lis.append(data.copy())

#print (lis)

print ()

if len(lis) == 1:
    print (f'Foi cadastrada somente uma pessoa')
elif len(lis) > 1:
    print (f'Foram cadastradas {len(lis)} pessoas')

print ()

print (f'A médida de idade dos cadastrados é {mean(med)}')

print ()

for c in range (0,len(lis)):
    if (lis[c]['idade']) > mean(med):
        medma.append(lis[c]['nome'])

if len(medma) == 1:
    print (f'O que tem a idade maior que a média é: ', end=' ')
    for c in range (0,len(medma)):
        print (medma[c])
  
elif len(medma) > 1:
    print (f'Os que tem a idade maior que a média são: ', end=' ')
    for c in range (0,len(medma)):
        print (medma[c], end=' ')
  
if len(mul) == 1:
    print (f'A mulher cadastrada foi: ', end=' ')
    for m in mul:
        print(m, end = ' ')

elif len(mul) > 1:
    print (f'As mulheres cadastradas foram: ', end=' ')
    for m in mul:
        print(m, end = ' ')
