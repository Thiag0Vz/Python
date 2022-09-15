def ficha(a = '',b = 0):
    if a == '':
        print (f'Jogador <desconhecido> fez {b} gol(s)')

    else: 
        print (f'Jogador {a} fez {b} gol(s)')
        
    if b == 0:
        print (f'Jogador {a} não fez nenhum gol')

a = str(input('Digite o nome do jogador: '))
b = str(input('Quantos gols ele fez? '))
if b.isnumeric():
    b = int(b) 
else:
    b = 0

ficha(a,b)