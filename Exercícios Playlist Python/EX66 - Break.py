n = 0
s = 0
c = 0
while (n != 999):
    print ('Digite um número')
    n = int(input())
    if (n == 999):
        break
    c += 1
    s = (s+n)
print (f'Foram digitados {c} números, e a soma é {s}')