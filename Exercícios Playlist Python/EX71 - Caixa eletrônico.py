print ('Quanto deseja sacar?')
n = int(input())
c50 = c20 = c10 = c1 = 0

while (n > 0):
        n -= 50
        c50 += 1

        if (n < 50):
            break
        
while (n > 0):
        n -= 20
        c20 += 1
        
        if (n < 20):
            break

while (n > 0):
        n -= 1
        c1 += 1

        if (n < 1):
            break 
print (f'Foram usadas {c50} notas de 50')
print (f'Foram usadas {c20} notas de 20')
if (c10 > 0):
    print (f'Foram usadas {c10} notas de 10')
print (f'Foram usadas {c1} notas de 1')