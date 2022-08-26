dic = {'nome': 'Thiago', 'sexo': 'M', 'idade': 19}
#Dicionários tem valores, keys e itens
print(dic.values()) #Valores são os valores "dentro" do dicionário
print(dic.keys())#Keys são as posições (como 0 e 1 em listas)
print(dic.items())#Items são os dois
print ('')
print (f'O nome é {dic["nome"]}, a idade é {dic["idade"]}')


for k,v in dic.items(): #Pra cada chave e valor em items:
    print (f'{k} é {v}')

print ('')

for k in dic.keys(): #Pra cada key em keys
    print(f'A chave é {k}')

#del dic['idade'] #del é o comando de remover
#print (dic)

dic['peso'] = 66 #Pra acrescentar novos elementos dentro de um dicionário, basta "declarar" ele no momento, junto com o dado 
#print (dic)

print ('')

#Dicionario dentro de lista
ls = []
estado1 = {'Estado': 'São Paulo'}
estado2 = {'Estado': 'Rio de Janeiro'}

ls.append(estado1)
ls.append(estado2)

print (ls) #Lista inteira
print (ls[0]) #Posição 0 da lista ({'Estado': 'São Paulo'})
print (ls[1]) #Posição 1 da lista ({'Estado': 'Rio de Janeiro'})
print (ls[0]['Estado']) #Dentro da posição 0, a key 'Estado'
print (ls[1]['Estado']) #Dentro da posição 1, a key 'Estado'


