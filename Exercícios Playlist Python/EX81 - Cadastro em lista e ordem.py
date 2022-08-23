from operator import invert


r = ''
ls = []
while (r != 'N'):
    print('Digite um número: ')
    n = int(input())
    ls.append(n)

    print ('Deseja continuar? S/N')
    r = str(input()).upper()


if (len(ls) > 1):
    print (f'Foram digitados {len(ls)} valores')
elif (len(ls) == 1):
    print (f'Foi digitado somente o valor {len(ls)}')

print (f'Em ordem decrescente, os valores foram: {sorted(ls, reverse = True)}')

if (ls.count(5) >= 1):
    print ('O valor 5 foi digitado e está na lista')
else:
    print ('O valor 5 não foi digitado')