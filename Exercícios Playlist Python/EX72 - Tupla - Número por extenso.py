print ('Digite um número entre 1 e 20')
n = int(input())

ext = ('um', 'dois', 'três', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
           'doze', 'treze', 'catorze', 'quinze', 'dezesseis',
           'dezessete', 'dezoito', 'dezenove', 'vinte')

while (n < 0) or (n > 20):
    print ('Inválido. Tente novamente.')
    print ('Digite um número entre 1 e 20')
    n = int(input())

print (f'Você digitou o número {ext[n-1]}')