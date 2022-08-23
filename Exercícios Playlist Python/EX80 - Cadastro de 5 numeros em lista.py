ls = []
c = 0


while (c < 5):
    print ('Digite um número: ')
    n =  int(input())
    c += 1
    
    if (c == 1) or (n > ls[-1]):
        ls.append(n)
    else:
         pos = 0 # Esse pos é para verificar conforme a posição da lista
         while pos < len(ls): #Enquanto a posição for menor que o número da lista - ou seja, vai andar até o final - vai verificar o seguinte:
            if (n <= ls[pos]): #Se n for menor igual ao número da lista na posição pos, ele vai inserir nessa posição e parar o programa. 
                ls.insert(pos,n)
                break
            print (ls) #Coloquei esse print pra facilitar a visualização do loop. Quando ele ocorre, significa que o número inserido foi maior, ou seja, não corresponde ao if

            pos += 1 #Se não for, vai acrescentar 1 e repetir o loop desde o início


print (f'Final {ls}')
