print ('Digite o primeiro valor')
n1 = float(input())

print ('Digite o segundo valor')
n2 = float(input())

d = 0 #Essa variável foi criada com o intuito de permitir o while abaixo
while (d != 7): #Esse while é o que faz o programa ficar em loop. Enquanto for diferente de 7, irá exibir o menu

    print ('')
    print ('O que deseja fazer?')
    
    print ('''
    [1] Somar
    [2] Subtrair
    [3] Multiplicar
    [4] Dividir
    [5] Maior valor
    [6] Digitar novos valores
    [7] Sair do programa''')
    
    d = int(input()) #Aqui o programa recebe a orientação sobre o que fazer, substituindo o valor de d na linha 7

    if (d == 1):
        var = (n1 + n2)
        print ('A soma é {}'.format (var))

    if (d == 2):
        var = (n1 - n2)
        print ('A substração é {}'.format (var))

    if (d == 3):
        var = (n1 * n2)
        print ('A multiplicação é {}'.format (var))

    if (d == 4):
        var = (n1 / n2)
        print ('A divisão é {}'.format (var))

    if (d == 5):
        if (n1 > n2):
            print ('{} é maior'.format (n1))
        elif (n2 > n1):
            print ('{} é maior'.format (n2))
  
    if (d == 6):
        print ('Digite o primeiro valor')
        n1 = float(input())

        print ('Digite o segundo valor')
        n2 = float(input())
print ('Encerrando...')
