print ('Digite um número')
n1 = int(input())

for c in range (1,n1+1):
    if (n1 % c == 0):
        print (c,' ', end = '')
