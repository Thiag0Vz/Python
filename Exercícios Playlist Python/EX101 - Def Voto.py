import datetime

def voto(x):
    ano = datetime.date.today()
    a = ano.year - x
    if a > 69 or a < 18 or a >= 16:
        print (f'Voto facultativo. Não é obrigatório.')
    else:
        if a > 18 and a <= 69:
            print (f'Voto obrigatório')


nas = int(input('Em que ano você nasceu? '))
voto(nas)