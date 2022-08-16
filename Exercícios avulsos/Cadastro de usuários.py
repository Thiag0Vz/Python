print ('Digite o usuário')
user = str(input())
print ('Digite a senha')
passw = str(input())
while (user == passw):
    print  ('Usuário não pode ser igual a senha')
    if (user == passw):
        print ('Digite o usuário')
        user = str(input())
        print ('Digite a senha')
        passw = str(input())
