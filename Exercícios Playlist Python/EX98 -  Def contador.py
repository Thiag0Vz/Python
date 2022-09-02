import time

def cont(i,f,p):
    print (f'Contagem de {i} até {f} de {p} em {p}')

    if p < 0:
        p = p*-1

    if p == 0:
        p = 1   

    if i < f:
        for a in range (i,f+1,p):
            #time.sleep(0.125)
            print (a, end=' ')
        print ('Fim! ')
    else:
        while i > f-1:
            print(f'{i}',end=' ')
            i -= p

        
print (f'Contador de 1 até 10 de 1 em 1')

for b in range(1,11):
    #time.sleep(0.125)
    print (b,end=' ')
print ('Fim!')

print()

print (f'Contador de 1 até 10 de 2 em 2')
for c in range(1,11,2):
    #time.sleep(0.125)
    print (c,end=' ')
print ('Fim!')

print()

print ('Sua vez de personalizar a contagem')
cont(i = int(input('Início: ')),f = int(input('Fim: ')),p = int(input('Passo: ')))