cad = {}
gols = []

cad['nome'] = str(input('Qual o nome do jogador? '))
n = int(input('Quantas partidas ele jogou? '))

for c in range (1,n+1):
    gols.append(int(input(f'Quantos gols na {c}° partida? ')))

cad['gols'] = gols
cad['total'] = sum(gols)
print (cad)

#print (cad.values())
#print (cad.keys())

for key,value  in cad.items():
    print (f'{key}: {value}')