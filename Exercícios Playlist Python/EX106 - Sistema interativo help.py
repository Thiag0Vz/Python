def sis(x):
   help(x)
   

comando = ''
while True:
    comando = str(input('Digite um comando: '))
    if comando.upper() == 'FIM':
        break
    else:
        sis(comando)