import itertools
from random import randint
import time
from operator import itemgetter

data = {}
rank = {}

for c in range (1,5): #De 1 a 4, vai fazer o seguinte:
    data[f'{c}'] = randint(1,6) #Aqui uma novidade:  dá pra colocar o nome das keys junto com o contador
print (data)





for a,b in data.items(): #Dentro de dos items de data, que são a junção da chave e valor, vai pegar o 
    #primeiro valor com o segundo valor
    print (f'Jogador {a} tirou: {b}')
    time.sleep(0.6)

    
rank = sorted(data.items(), key=itemgetter(1), reverse=True) #Aqui está sendo criado o ranking
#itemgetter(1) vai pegar, dentro de sorted data, o valor na posição 1
print ()
for i,v in enumerate(rank):
    print (f'{i+1}° Lugar Jogador {v[0]}, que tirou {v[1]}')






'''for v,m in data.items():
    if data[f'{c}'] < ma:
        ma = data[f'{c}']
print (ma)
'''
