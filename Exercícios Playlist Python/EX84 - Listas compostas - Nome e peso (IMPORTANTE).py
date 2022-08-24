r = ''
data = [] #Base de dados temporária
base = [] #Base de dados
mp = mn = 0 #Maior e menor peso


while r != 'N':
    data.append(str(input('Digite seu nome: ')))
    data.append(float(input('Digite seu peso: ')))

    if len(base) == 1: #Se o tamanho da base for = a 0, significa que é o primeiro elemento
        mp = mn = data[1] #Sendo o primeiro elemento, será o maior e menor ao mesmo tempo
    else:
        if data[1] > mp: #Se o peso for maior que o maior peso, o maior peso passa a ser peso 
            mp = data[1]
        
        if data[1] < mn:#Se o peso for menor que o menor peso, o menor peso passa a ser peso 
            mn = data[1]

    base.append(data[:]) #Faço uma cópia da lista data para a lista base
    data.clear() #Limpo a lista data e retorno o loop
    r = str(input('Deseja continuar? S/N ')).upper()

print (f'Foram cadastradas {len(base)} pessoas')
print(f'O maior peso foi {mp} e o menor foi {mn}')



    #print (f'O peso de {p[0]} é {p[1]}')