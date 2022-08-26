#Listas dentro de listas

'''ls = [['Carlos', 12], ['Hen', 14]]
ls2 = [['Maria',19]]
print (ls[0]) #Mostrando a posição 0 de ls 
print (ls[0][1]) #Dentro de ls, dentro do elemento 0, pegando a posição 1


ls.append(ls2[0])
print (ls)
'''



galera = []
data = []

for c in range (0,2):
    data.append(str(input('Nome: '))) #Está acrescentando na lista juntamente com o input
    data.append(int(input('Idade: '))) #Está acrescentando na lista juntamente com o input
    galera.append(data[:]) #Está fazendo uma cópia da lista. Dessa forma, elas não ficam conectadas
    data.clear()#Quando chega no final, os dados são "transportados" de data para galera, e excluídos de
    #Se ficassem conectadas, quando desse clear, seriam apresentadas listas vazias
#print (galera) #Está mostrando a base que foi criada com os appends. 
print (galera)
print (galera[1])
totmai = 0
totmen = 0

for p in galera: #O FOR PASSA POR CADA ITEM DA LISTA. P é somente a variável de controle.
    if p[1] >= 21:
        print (f'{p[0]} é maior de idade e tem {p[1]} anos')
        totmai += 1
    else: 
        print (f'{p[0]} é menor de idade e tem {p[1]} anos')
        totmen += 1
print (f'Existem {totmai} maiores de idade e {totmen} menores de idade')