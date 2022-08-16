m = 0
mr = 0
mn = 0
s = 0
c = 0
ch = ''

while (ch != 'N'):
    print ('Digite um número: ')
    n = int(input())
    s = (s+n)
    c += 1
    m = (s/c)
    if (c == 1):
        mr = mn = n
    else:
        if (n > mr):
            mr = n
        if (n < mr):
            mn = n

    print ('A média dos valores digitados é {}, o maior valor é {} e o menor é {}'.format(m,mr,mn))
    print ('')
    print ('Deseja continuar? S/N')
    ch = str(input()).upper()
print ('Encerrando o programa')