import random
import time

n = int(input('Quantos jogos quer que eu sorteie? '))
cont = 0
ls = []
temp = []

while cont < n: #Enquanto o contador for menor que o número que o usuário pediu, irá executar
    while len(temp) < 6: #Enquanto o tamanho da lista temp for menor que 6, será adicionado um número aleatório a lista
        temp.append(random.randint(1,60)) #Função random para adicionar um aleatório na lista
    ls.append(temp[:]) #Aqui faço uma cópia da lista temp para a lista ls, onde será armazenado
    temp.clear() #Limpo a lista temporária e repito o loop  
    cont += 1 #O contador recebe 1, retornando ao loop até atingir a condição

#print (temp)
#print (f'ls {ls}')

for c, v in enumerate(ls): #Em c, para cada valor em ls, será criada exibida a posição v em ls
    time.sleep(0.5)
    print (f'Jogo {c+1}: {v}')

        
    



        

