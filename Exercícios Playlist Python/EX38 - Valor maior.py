print ('Digite o primeiro número')
n1 = int(input())

print ('Digite o segundo número')
n2 = int(input())

if (n1 == n2):
    print ('Não existe valor maior, pois são iguais')
elif (n1 > n2):
    print ('{} é maior'.format (n1))
elif (n2 > n1):
    print ('{} é maior'.format (n2))