#Interactive help

#help() #Quando chamamos a função help(), o prompt é aberto e podemos colocar qualquer comando que temos dúvidas
#Pra sair do prompt basta digitar "quit"

#help(print) #Outra forma de usar help().



#Docstrings
#Docstrings são as "instruções" de uma definição, seja ela nativa ou criada.
#Podemos criar as próprias docstrings nas definições, só precisamos de 3 aspas na primeira linha da def
def docstr():
    """
    Essa é a doc string de docstr.
    """

#help(docstr)



#Argumentos opcionais
#Basta igualarmos as variáveis da def como 0

def optarg(a = 0, b = 0):
    s = a + b
    #print (s)
optarg(1)



#Escopo de variáveis
#Quando criamos 

def esc():
    print(f'Na função, n vale {n}')
    x = 8
    print(f'Na função, x vale {x}')
    
#Principal
n = 2 
print (f'No programa principal, n vale {n}')
esc() #Mesmo n tendo sido definida no programa principal, também se aplicou à função.
#Isso é escopo global. 
print(f'Na função, x vale {x}') #Isso não dá certo porque x só existe dentro da definição.
#Isso é escopo local. 
#Podemos ter duas ou mais variáveis "iguais", desde que em escopos diferentes
def escop():
    #n = 1 #Aqui temos o n da def, enquanto que na linha 41 temos n do programa principal
    #Pra usar o n global, teria que ser:
    global n 



#Return
#Return retorna o resultado. É bom pra exibir respostas personalizadas.
#Pra usar o return, precisa de uma variável ou podemos usar direto dentro da função

def ret(a = 0, b = 0):
    s = a + b
    return s

r1 = ret(1,2)
r2 = ret(5,2)
r2 = ret(1,21)
#Ou
print(f'{r1},{r1},{r1}')