from unicodedata import numeric

def intver(x):
    '''
    Essa função verifica se o valor inserido é um valor inteiro.
    O argumento x trata-se do input do usuário    
    '''
    verif =  False #Verificação por padrão é falsa
    valor = 0 #Valor é zero

    while True: 
        n = str(input(x)) #n local vai receber o valor de x como uma string
        if n.isnumeric(): #Vai verificar se a string n é numérica
            valor = int(n) #Se for numérica, valor vai receber como inteiro 
            verif = True #verificação recebe True
        else:
            print ('Valor inválido') #Se não for um número
            
        if verif == True: #Aqui não precisa desse == True, mas coloquei pra ilustrar. Se verif estiver "OK", vai encerrar o while
            break

    return valor #Retorna o valor para a def


def floatver(x):

    #Essa função verifica se o valor inserido é um valor inteiro.
    #O argumento x trata-se do input do usuário

    verif = False  # Verificação por padrão é falsa
    valor = 0  # Valor é zero

    while True:
        n = str(input(x))  # n local vai receber o valor de x como uma string
        if n.isnumeric():  # Vai verificar se a string n é numérica
            valor = float(n)  # Se for numérica, valor vai receber como inteiro
            verif = True  # verificação recebe True
        else:
            print('Valor inválido')  # Se não for um número

        if verif == True:  # Aqui não precisa desse == True, mas coloquei pra ilustrar. Se verif estiver "OK", vai encerrar o while
            break

    return valor  # Retorna o valor para a def


n = intver('Digite um número: ')
f = floatver('Digite um número float: ')

print (f'O valor digitado foi {n}')
print (f'O valor float digitado foi {f}')