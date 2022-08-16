tup = ('Palmeiras', 'Corinthians', 'Fluminense', 'Athletico-PR', 'Flamengo',
        'Internacional', 'Atlético-MG','Bragantino', 'América-MG','Santos',
        'São Paulo','Botafogo','Goiás','Ceará SC', 'Coritiba','Avaí','Fortaleza',
        'Cuiabá','Atlético-GO','Juventude')

print ('Os 5 primeiros colocados são: ')
print (tup[1:6])

print ('Os 4 últimos colocados são: ')
print (tup[-5:])

print ('Em ordem alfabeta, temos: ')
print(sorted(tup))

c = 0

while (tup[c-1] != 'São Paulo'):
    c += 1
print (f'Está na posição {c}')