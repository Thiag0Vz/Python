cad = {}
gols = []
r = ''
data = []

while r != 'N':
    
    cad['nome'] = str(input('Qual o nome do jogador? '))
    print ()
    n = int(input('Quantas partidas ele jogou? '))

    for c in range (0,n):
        gols.append(int(input(f'Quantos gols na {c+1}° partida? ')))
        cad['gols'] = gols[:]
    cad['total'] = sum(gols)
    data.append(cad.copy())
    gols.clear()
     
    r = str(input('Deseja continuar? S/N ')).upper()

#print (data)

for c in range (0,len(data)):
    print (data[c]['nome'], end=' ')
    print (data[c]['gols'], end=' ')
    print (data[c]['total'], end=' ')
