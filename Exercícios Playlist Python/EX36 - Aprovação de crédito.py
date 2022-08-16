print ('Programa de aprovação de crédito bancário')

print ('Qual o valor da casa?')
vc = float(input())

print ('Valor do seu salário')
sal = float(input())

print ('Em quanto anos vai pagar?')
ano = int(input())


prest = (vc/(ano*12))
print ('O valor da prestação é de R$ {}'.format (prest))

if (prest*0.3) > sal:
    print ('O crédito não foi aprovado pois a prestação excede 30% do seu salário')
else:
    print ('O crédito foi aprovado!') 