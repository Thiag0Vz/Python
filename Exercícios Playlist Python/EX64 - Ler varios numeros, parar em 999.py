n = 0
c = 0
s = 0
while (n != 999):
    print ('Digite um número')
    n = int(input())
    if (n != 999):
        s = (s+n)
    if (n != 999):
        c += 1
print ('Fim do programa. Foram digitados {} números. A soma deles é de {}'.format(c,s))

