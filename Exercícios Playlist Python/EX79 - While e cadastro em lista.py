r = ''
lis = []
while (r != 'N'):
    print ('Digite um número: ')
    n = int(input())
    
    if n not in lis:
        lis.append(n)
    else:
        print ('Este número já existe na lista')
    print ('Deseja continuar? S/N')
    r = str(input()).upper()
print (sorted(lis))


