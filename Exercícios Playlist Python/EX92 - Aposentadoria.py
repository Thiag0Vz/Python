import datetime

cad = {}
ano = datetime.date.today()
print (ano.year)

cad['nome'] = str(input('Digite seu nome: '))
cad['nasc'] = int(input('Digite sua data de nascimento: '))
cad['idade'] = ano.year - cad['nasc']
cad['gen'] = str(input('Digite seu gênero: M/F ')).upper()
cad['ctps'] = int(input('N° Carteira de trabalho (0 caso não tenha): '))


if cad['ctps'] != 0:
    cad['anocontr'] = int(input('Digite o ano de contratação: '))
    cad['sal'] = float(input('Digite seu salário: R$ '))
    if cad['gen'] == 'M':
        cad['apos'] = cad['anocontr'] + 35
    elif cad['gen'] == 'F':
        cad['apos'] = cad['anocontr'] + 30
else:
    del cad['ctps']


print(cad)

for v,k in cad.items():
    print(f'{v}: {k}')