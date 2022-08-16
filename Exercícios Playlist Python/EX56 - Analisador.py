sumid = 0
medid = 0
homvelid = 0
nomvel = ''
mul = 0

for i in range (1,5):
    print ('Qual é o nome do {}° indivíduo?'.format(i))
    nm = str(input())
    print ('Quantos anos tem?')
    id = int(input())
    print ('Qual gênero? M/F?')
    gen = str(input())

    if (i == 1) and (gen in 'Mm'): 
        homvelid = id
        nomvel = nm

    if (gen in 'Mm') and (id > homvelid):
        homvelid = id
        nomvel = nm

    if (gen in 'Ff') and (id < 20):
        mul = mul+1

    sumid = (sumid + id) #Aqui todas as idades serão acumuladas
    medid = (sumid/i)

print ('A média de idade é {}'.format(medid))

if (gen in 'Mm'):
    print ('O homem mais velho é {} e tem {} anos'.format(nomvel, homvelid))

if (mul > 0):
    print ('Existem {} mulheres menores de 20 anos'.format (mul))