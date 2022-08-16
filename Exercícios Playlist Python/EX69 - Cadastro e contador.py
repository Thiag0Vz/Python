from datetime import datetime

c18 = 0
cm = 0
cmu = 0
cm20 = 0
an = datetime.now().year
p = ''

while True:
    while (p != 'N'):
        print ('Em que ano você nasceu?')
        nas = int(input())
        id = (an-nas)

        print ('Qual seu gênero? (M/F)')
        gen = str(input()).upper()

        print ('Deseja continuar? (S/N)')
        p = str(input()).upper()
        if (id > 18):
            c18 += 1
        if (gen == 'M'):
            cm += 1
        if (gen == 'F'):
            cmu += 1
        if (gen == 'F') and (id < 20):
            cm20 += 1
    break 

print (f'Existem {c18} pessoas com mais de 18 anos')
print (f'Foram cadastrados {cm} homens')
print (f'Foram cadastrados {cmu} mulheres')
print (f'{cm20} mulheres tem menos de 20 anos')

        