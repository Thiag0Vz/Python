n = 1
while (n > 0):
    print ('Digite o número da tabuada')
    n = int(input())
    if (n < 0):
        break
    for m in range(1,11):
        mul = (n*m)
        print (n,'*',m,'=',mul)
print ('O número digitado é inválido. Encerrando...')