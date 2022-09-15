def fat(x,show=False):
    f = 1
    for c in range (x,0,-1):
        f *= c
    print ()
    print (f)
    print ()
    if show == True:
        for c in range (x,0,-1):
            print (f'{c} * ',end=' ')
        print(f'= {f}',end='')

a = int(input('Digite o número que quer fatorar:'))       
b = str(input('Deseja ver o processo de fatoração? S/N ')).upper()

if b == 'S':
    b = True 
elif b == 'N':
    b = False   
    
fat(a, b)