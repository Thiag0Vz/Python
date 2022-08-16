from datetime import date
ayr = date.today().year
totma = 0
totme = 0

for i in range (1, 8):
    print ('Qual a {}° data de nascimento?'.format(i))
    nasc = int(input())
    if (ayr - nasc >= 21):
        totma +=1
    elif (ayr - nasc <= 21):
        totme +=1

print ('Existem {} maiores de idade'.format(totma))
print ('e {} menores de idade'.format(totme))