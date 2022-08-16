from ctypes import sizeof
from itertools import count
print ('Digite seu nome')
nm = str(input())

while (len(nm) < 3): 
  if (len(nm) < 3):
    print ('Invalido')
    print ('Digite seu nome')
    nm = str(input())

print ('Digite sua idade')
id = int(input())

while (id < 0) or (id > 100):
    if  (id < 0) or (id > 100):
        print ('Idade inválida')
        print ('Digite sua idade')
        id = int(input())

print ('Informe seu salário')
sal = float(input())

while (sal <= 0):
    if  (sal <= 0):
        print ('Salário inválido')
        print ('Informe seu salário')
        sal = float(input())

print ('Informe seu gênero M/F')
gen = str(input())

while (len(gen)>1) or (gen != 'M') and (gen != 'F'):
    if (len(gen)>1) or (gen != 'M') and (gen != 'F'):
        print ('Isso Non Ecziste!')
        print ('Informe seu gênero M/F')
        gen = str(input())

print ('Informe seu Estado Civil (S/C/V/D)')
estc = str(input())

while (len(estc)>1) or (estc != 'S') and (estc != 's') and (estc != 'C') and (estc != 'c') and (estc != 'V') and (estc != 'v') and (estc != 'D') and (estc != 'd'):
    if (len(estc)>1) or (estc != 'S') and (estc != 's') and (estc != 'C') and (estc != 'c') and (estc != 'V') and (estc != 'v') and (estc != 'D') and (estc != 'd'):
        print ('Estado Civil inválido!')
        print ('Informe seu Estado Civil (S/C/V/D')
        estc = str(input())