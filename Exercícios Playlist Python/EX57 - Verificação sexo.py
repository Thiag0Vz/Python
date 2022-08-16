print ('Digite seu sexo (M/F)')
sx = str(input()).upper()

while (sx != 'M') and (sx != 'F'):
    print ('Inválido. Digite novamente.')
    print ('Digite seu sexo (M/F)')
    sx = str(input()).upper() 
print ('Obrigado')