tup = (int(input()),int(input()),int(input()),int(input()),int(input()))


if (tup.count(9) == 1):
    print (f'O valor 9 aparece {tup.count(9)} vez')
elif (tup.count(9) > 1):
    print (f'O valor 9 aparece {tup.count(9)} vezes')
else:
    print ('O valor 9 não apareceu nenhuma vez na sequência.')

if (3 in tup):
    print (f'O valor 3 foi digitado na posição {tup.index(3)}')
else:
    print ('Não teve valor 3')

print (f'Os valores pares digitados foram', end = ' ')
for n in tup:
    if (n%2 == 0):
        print (f'{n}', end = ' ')

