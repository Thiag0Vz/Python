import time
print ("Vamos jogar um jogo de adivinhação? S/N")
r = input()
if r == ('s' or 'S'):
    time.sleep(1.2)
    print ('Vou pensar em um número de 1 a 10... Espere um pouco.')
    time.sleep(0.7)
    print ('Processando...')

    time.sleep(3.5)

    from random import randint
    n =  randint(1,10)

    print ('Em que número pensei? ')
    result = int(input())
    if result == n:
        print ('Você acertou!')
    else:
        print ('Errou!. O número que pensei foi {}'.format(n))
else:
    if r == ('n' or 'N'):
        time.sleep(1.2)
        print ('Ok, tchau tchau!')