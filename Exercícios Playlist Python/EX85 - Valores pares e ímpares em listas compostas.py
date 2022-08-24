ls = [[],[]]
tempp = []

for c in range(0,6):
    n = int(input('Digite um número: '))
    
    if n%2 == 0:
        tempp.append(n)
        ls[0].append(tempp[:])
        tempp.clear()
    else:
        tempp.append(n)
        ls[1].append(tempp[:])
        tempp.clear()

print (f'Os valores pares digitados foram {ls[0]}')
print (f'Os valores impares digitados foram {ls[1]}')