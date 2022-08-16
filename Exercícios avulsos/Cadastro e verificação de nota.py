n = -1
while (n < 0) or (n > 10):
    print ('Digite uma nota')
    n = float(input())
    if (n < 0) or (n > 10):
        print ('Valor inválido')
print ('O valor digitado foi {}'.format(n))