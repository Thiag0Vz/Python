estado = {}
brasil = []

for c in range(0,2):
    estado['uf'] = str(input('Digite a Unidade federal: ')) #Crio o campo "uf" e insiro o dado
    estado['Sigla do Estado: '] = str(input('Digite a sigla do Estado: ')) #Crio o campo "Sigla" e insiro o dado
    brasil.append(estado.copy()) #Não é possível utilizar [:]. Pra isso existe o copy()

print ()
print (f'A base de dados completa é {brasil}')
print ()

#Este programa basicamente cria listas com dicionários

for e in brasil: #Pra cada Estado do Brasil, mostra um dicionário
    #print (e)
    for k in e.values(): #Pra cada key em Estado
        print (k, end=' ')