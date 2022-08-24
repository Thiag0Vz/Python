r = ''
data = [] #Base de dados temporária
base = [] #Base de dados
mp = mn = 0 #Maior peso
mpr = [] #Maiores pesos registrados

while r != 'N':
    data.append(str(input('Digite seu nome: ')))
    data.append(float(input('Digite seu peso: ')))

    if len(base) == 0:
        mp = mn = data[1]
    else:
        if data[1] > mp:
            mp = data[1]
        
        if data[1] < mn:
            mn = data[1]

    base.append(data[:])
    data.clear()
    r = str(input('Deseja continuar? S/N ')).upper()

print (f'Foram cadastradas {len(base)} pessoas')

for p in base:
    if p[1] > mp:
        mpr.append(p[1])
        mp = p[1]
print(f'O maior peso foi {mp} e o menor foi {mn}')



    #print (f'O peso de {p[0]} é {p[1]}')