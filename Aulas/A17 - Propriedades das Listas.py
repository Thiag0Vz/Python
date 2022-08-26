import enum


lis = [1,1,10,12,5,6,14,21]
lis_2 = ['Thiago','Carlos']
lis_3 = [1,10,12,5,1,6,14,21]


del lis[6] #Eliminando o 6° elemento de lis
lis.pop #Serve para eliminar o último elemento, mas também podemos selecionar qual elemento exclui
lis.pop(6)

lis_2.remove('Carlos') #No remove não se especifica o índice, mas sim o item que quer remover da lista


lis.append('Teste') #Adiciona elementos de qualquer natureza no final da lista

lis.extend(lis_2) #"Integra" outros elementos, como listas ou strings. Meio que soma as duas

print (lis_3.sort()) #Coloca os elementos em ordem, mas só funciona com valores ou strs separadamente
#print ('Essa é a Lista 3',lis_3)

lis_2.sort() #Coloca os elementos em ordem, mas só funciona com valores ou strs separadamente
#print ('Essa é a Lista 2',lis_2)

lis.insert(1,999) #Insere elementos na lista, substituindo-os. O primeiro argumento é a posição, o segundo, o valor a ser aplicado

#print (lis.count(1)) #Conta a ocorrência de valores

#lis.pop() #Remove o último elemento. Os valores colocados se referem a posição na lista

lis.remove(10) #Quase igual ao pop, porém se refere ao elemento e não à posição

#lis.clear() #Esvazia a lista

print (lis.index(12)) #Exibe a posição de um item na lista. Dá pra colocar argumentos dentro.
#print (lis)
#sorted(lis, reverse=True) # o sorted cria uma lista com os valores em ordem, seja crescente ou decrescente
'''for v,c in enumerate(lis_3):
    print (f'{c} está na posição {v}')'''

#Conexão entre listas
a = [2,4,5,6]
b = a
#b[2] = 8 #Nesse caso, ao contrário do que se possa dedudizir, as duas listas serão alteradas ao invés de somente a b ser alterada, já que elas estão "conectadas".
#Pra corrigir isso, usa-se [:] que significa receber todos os itens do elemento em questão
b = a[:]
b[2] = 8

 
print (f'Lista A: {a}')
print (f'Lista B: {b}')