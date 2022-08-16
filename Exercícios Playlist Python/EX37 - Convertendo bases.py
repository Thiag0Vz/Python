print ('Digite um número')
n1 = int(input())

print ('Qual será a base de conversão?')

print ('1 - Binário')
print ('2 - Octal')
print ('3 - Hexadecimal')

ch = int(input())

if (ch == 1):
    print ('Ok. Vamos converter para binário')
    n1 = bin(n1)
    n1 = format(10,"b")
    print (n1)
elif (ch == 2):
    print ('Ok. Vamos converter para octal')
    n1 = str(oct(n1))
    print (n1)
elif (ch == 3):
    print ('Ok. Vamos converter para hexadecimal')
    n1 = str(hex(n1))
    print (n1)

