print ("Hi. Whats your name? ")
name=input()
print ("Cool {}. Can i make a few questions? y/n ".format(name)) #Colocar + opções de resposta #Se colocar números, voltar ao IF
r = str(input())
if r == 'y': #Colocar + opções de resposta #Se colocar números, voltar ao IF
        print ("Great")
else:
    if r == 'n':
        print ("Ok... :(")
        exit()

print ("Male or Female? m/f ") # verificar se é f ou m e se não for, retornar.
sx = str(input())

print ("How old are you? ")
r1 = int(input())

if r1>89:
    print ("Do you really have {} years? y/n".format(r1))
    v = input()
    if v == 'y':
        print ("Ok...")
    else:
        if v == 'n': #retornar ao if de idade
            print ("hahaha very funny.")


if r1 <=20:
    print ("Nice, you're very young")
else:
    print ("So you´re already an adult...")

if r1<=10:
    print ("You´re too young to use this program! ")
    exit()
        
wt = float (input ("Whats your weight? "))
ht = float (input("... and your height? "))
print ("Ok.")

bmi = wt/(ht*ht)
print ("You BMI are: ",bmi)

if sx == 'f': #female
    if bmi<=19.1:
        print ("You´re under ideal weight :(")     
    elif bmi>=19.2 and bmi<=25.8:
        print ("You´re in ideal weight! ")   
    if bmi>=25.9 and bmi<=27.3:
        print ("You are a little bit above ideal weight...")
    elif bmi>=27.4 and bmi<=32.3:
        print ("You should consider stopping going to McDonalds")
    if bmi>32.3:
        print ("You are a land whale.")

if sx == 'm': #male
    if bmi<=20.7:
        print ("You´re under ideal weight :(")
    elif bmi>=20.8 and bmi<=26.4:
        print ("You´re in ideal weight! ")
    if bmi>=26.5 and bmi<=27.8:
        print ("You are a little bit above ideal weight...")
    elif bmi>=27.9 and bmi>=31.1:
         print ("You should consider stopping going to McDonalds")
    if bmi>31.2:
        print ("Such a fatass")
        exit()
        
