import time

print ('Podemos iniciar a contagem? S/N')
r = str(input())

if (r == 's') or (r == 'S'):
    for c in range (10,0,-1):
        time.sleep(1)
        print (c)
    print ('POUPOWTATATAFIII')
elif (r == 'n') or (r == 'N'):
    print ('Ok.')
    