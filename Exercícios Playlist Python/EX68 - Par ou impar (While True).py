import random
import time
c = 0
print ('Jogo de par ou ímpar')
while True:
    
    print ('Digite um número')
    n =  int(input())

    print ('Você quer Par ou Ímpar? (P/I)')

    e = str(input()).upper().strip()
    a = random.randint(0,10)
    s = (a+n)

    if (e == 'P'):
        if (s%2 == 0):
            print (f'Você ganhou. O computador escolheu {a}')
            c += 1
        else:
            print (f'Você perdeu. O computador escolheu {a}')
            break
    elif (e == 'I'):
        if (s%2 != 0):
            print (f'Você ganhou. O computador escolheu {a}')
            c += 1
        else:
            print (f'Você perdeu. O computador escolheu {a}')
            break
print (f'Foram {c} vitórias consecutivas')