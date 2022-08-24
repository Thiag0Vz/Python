r = ''
ls = []
lsp = []
lsi = []

while (r != 'N'):
    print('Digite um número: ')
    n = int(input())
    ls.append(n)

    print ('Deseja continuar? S/N')
    r = str(input()).upper()

pos = 0
while (pos < len(ls)):
    if (ls[pos]%2 == 0):
        lsp.append(ls[pos])
    elif (ls[pos]%2 != 0):
        lsi.append(ls[pos])
    pos += 1

print (f'A lista digitada foi {ls}')
if (len(lsp) > 0):
    print (f'Os elementos pares foram {lsp}')

if (len(lsi) > 0):
    print (f'Os elementos ímpares foram {lsi}')