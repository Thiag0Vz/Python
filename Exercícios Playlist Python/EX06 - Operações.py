''' #numero antecessor
n = int(input ("Write a number: "))
print ("O antecessor do seu número é {}, e o sucessor é {}".format (n-1,n+1))
print ("Nice!")
n2 = int(input("Escreva outro!: "))
print ("O dobro do seu número é {}, o triplo {} e a raiz quadrada é {}".format(n2*2,n2*3,n2**2))
'''
''' #media de notas
nt1 = int(input("Agora duas notas do aluno: "))
nt2 = int(input())

print ("A média entre as notas é: {}".format((nt1+nt2)/2))
'''
''' #metros pra cm e mm
m = float(input("Digite uma metragem: "))
print ("{} em centímetros é: {} \n Já em milímetros é: {}".format(m,m*100,m*1000))
'''
''' #Tabuada
mult = int(input("Digite um número qualquer: "))
print ("A tabuada desse número: ")
print (mult * 1)
print (mult * 2)
print (mult * 3)
print (mult * 4)
print (mult * 5)
print (mult * 6)
print (mult * 7)
print (mult * 8)
print (mult * 9)
print (mult * 10)
'''
''' #cambio
val = float(input("Quantos reais você tem? "))
print ("Você possui o equivalente à {:.2f} dólares".format(val/5.37))
'''
alt = float(input("Qual a altura da parede em metros?"))
larg = float (input("E a largura?"))
print ("A área é de {.:2}, e você precisa de {.:2} litros de tinta.".format (alt*larg,(alt*larg)/4))
