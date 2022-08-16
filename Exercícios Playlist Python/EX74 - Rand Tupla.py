import random
menor = 0
c = 0
rn = (random.randint(1,5), random.randint(1,5), random.randint(1,5), random.randint(1,5), random.randint(1,5))

print (f'Os números gerados foram {rn}')

print ('O maior sorteado foi',max(rn),'O menor',min(rn))