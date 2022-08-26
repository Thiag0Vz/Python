data = {}

data['nome'] = str(input('Digite o nome: '))
data['media'] = float(input('Digite a média: '))
if data['media'] < 5:
    data['situação'] = 'reprovado'
else:
    data['situação'] = 'aprovado'

for k,v in data.items():
    print (f'{k} é igual a {v}')
