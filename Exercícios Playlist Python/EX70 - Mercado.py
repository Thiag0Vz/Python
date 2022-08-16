tot = cont = cont2 = menor = 0
ch = ''
p = ''
while True:
    while (p != 'N'):
        print ('Digite o nome do produto')
        prd = str(input())
        
        print ('Digite o preço do produto')
        prc = float(input())
        tot = (tot + prc)
        cont2 += 1

        if (prc > 1000):
            cont += 1

        if (cont2 == 1) or (prc < menor):
            menor = prc
            ch = prd

        print ('Deseja acrescentar mais produtos? (S/N)')
        p = str(input()).upper()
    break
print (f'O total gasto é de: R$ {tot}')
if (cont > 0):
    print (f'{cont} Custam mais que R$ 1000,00')
print (f'O mais barato é {ch} e custa {menor}')
