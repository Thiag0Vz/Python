print ('Choose the speed unity: ')
print ('1. Kmh')
print ('2. Mph')
un =  int(input())

print('What was the speed of vehicle? ')
spd = float(input()) 

if un == (1):
    if spd > 80:
            fin = (spd-80)*7
    print ('You will be fined in U$ {}'.format(fin))
else:
        print ('Ok, you´re safe')

if un == (2):
    if spd > 49.7:
        fin = (spd-49.7)*7
        print ('You will be fined in U$ {}'.format(fin))
    else:
        print ('Ok, you´re safe')
