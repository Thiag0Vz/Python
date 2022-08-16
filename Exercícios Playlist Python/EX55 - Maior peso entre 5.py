maior = 0
menor = 0
for i in range (1, 4):
    print ('Digite o peso do {}° indivíduo'.format(i))
    p = float(input())
    if (i == 1):
        maior = p
        menor = p
    else:
        if (p > maior):
            maior = p
        if (p < menor):
            menor = p
print ('O maior peso é {}'.format(maior))
print ('O menor peso é {}'.format(menor))