print ('Digite a população do primeiro País')
pa = int(input())
print ('Digite a população do segundo País')
pb = int(input())

i = 0
tx = 15
while (pa <= pb):
    if (pa <= pb):
        pa = (pa + (pa * (tx/100)))
        i = (i+1)
print (f'Serão necessários {i} anos para a população de A ser igual a de B, numa taxa de crescimento de {tx}%')
