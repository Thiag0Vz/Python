from random import randint
ls = []
par = []

def sorteia():
    for c in range (0,5):
        ls.append(randint(0,100))
    print ('Os números sorteados foram: ')
    print (ls)

def somapar():
    s = 0
    for c in ls:
        if c%2 == 0:
            #print (c,end=' ')
            par.append(c)
            s = c+s
    print ()
    print ('Os pares foram: ')
    for c in par:
        print (c)
        
    print ()
    print (f'A soma dos pares é {s}')

sorteia()
somapar()