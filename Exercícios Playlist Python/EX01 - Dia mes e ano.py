nome = input ('Qual seu nome? ')

print ('Olá',nome ,',muito bom ter você aqui. Pode me passar algumas informações?')

resposta = (input ('s/n '))

if resposta == 's':
    dia = input ('Que bom! Que dia você nasceu? ')
    mes = input ('E o mês? ')
    ano = input ('De que ano? ')
    #anoat = input ('E em que ano estamos? ')

if resposta == 'n' :
     print ('Pôxa, que pena.')

print ('Legal, você nasceu em ',dia,'/',mes,'/',ano)
resposta2 = input ('Podemos fazer mais uma coisinha? s/n ')
if resposta2 == 's':
 n1 = float (input ('Ótimo, me informe um número '))
 n2 = float (input ('Mais um, por favor '))
 s = n1+n2
print ('A soma é: ',s)
    

    
