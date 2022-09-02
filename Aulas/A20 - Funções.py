#FUNÇÕES (Parte 1) - Aula 20


#O que é uma FUNÇÃO no Python?
#São blocos nomeados de um código designado para fazer um trabalho em específico. Elas permitem que você escreva o código uma vez que
#poderá ser usado a quantidade de vezes que você precisar para fazer uma mesma função. As funções podem pegar a informação que elas precisam e retornar a informação que elas geram. Então, basicamente é um jeito de tornar os programas fáceis de escrever, ler, testar, e consertar.


#Para definir uma função, a primeira linha dela é a sua definição, marcada pela palavra-chave DEF. O nome da função é seguido por um conjunto
#de parênteses e dois pontos. Uma DOCSTRING, em aspas triplas, descreve o que a função faz. O corpo da função ou o bloco de códigos dela é identado em um nível.

#Exemplo:
def lin():
    """Mostra uma linha com trinta hífens seguidos."""
    print('-' * 30)

#Para chamar uma função, é só você digitar o nome da função seguido por um conjunto de parênteses, como por exemplo: lin()

#PARÂMETROS: INFORMAÇÃO QUE É RECEBIDA POR UMA FUNÇÃO, ESTÃO LISTADOS EM PARÊNTESES NA DEFINIÇÃO DA FUNÇÃO.

##ARGUMENTOS: INFORMAÇÃO QUE É PASSADA PARA UMA FUNÇÃO, SÃO INCLUÍDOS NOS PARÊNTESES DEPOIS DO NOME DA FUNÇÃO.
# 
#(Você pode tratar do jeito que você quiser, eu prefiro separar em parâmetros e argumentos.)
#
#*Exemplo de argumentos e parâmetros em uma função:
def mostra_titulo(texto):   # => texto nesse caso é o PARÂMETRO.
    """Mostra o título de forma elegante."""
    print(f'{"=-=" * 10}\n{texto.upper():^30}\n{"=-=" * 10}')


mostra_titulo('sistema de alunos')   # => 'sistema de alunos' é uma string que eu defini como ARGUMENTO.#
#*Existem dois tipos de argumentos, que são os posicionais e os argumentos de palavra-chave. Quando você usa argumentos posicionais, Python 
#orresponde ao primeiro argumento na chamada da função com o primeiro parâmetro na definição da função e assim por diante. Com os argumentos de palavra-chave, você específica com qual parâmetro o argumento deve ser atribuído na chamada da função. Quando os argumentos de palavra-chave são usados, a ordem dos argumentos não importa.
#
#
#*Exemplos de argumentos posicionais e de palavra-chave:
def mostra_soma(a, b):
    """Mostra a soma de dois números."""
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')

mostra_soma(4, 5)   #=>Argumentos posicionais.
mostra_soma(b=4, a=5)   #=> Argumentos de palavra-chave.

#Para passar um número arbitrário de argumentos para um parâmetro, usa-se o operador *. O parâmetro que deve aceitar um número arbitrário
 #de argumentos deve ser o último na definição de uma função. 

#Exemplo:
def contador(*num):
    """Mostra uma quantidade arbitrária de valores em uma tupla."""
    print(num)


contador(2, 1, 7)
contador(4, 4, 7, 6, 2)

#Você pode passar uma LISTA como argumento para uma função, e a função pode trabalhar com os valores na lista. Qualquer alteração feita na
 #lista criada pela função afetará a lista original. Para impedir que uma função modifique a lista original, é só passar como argumento uma cópia da lista.

#Exemplo, passando uma lista como argumento:
def dobra(lista):
    """Dobra os valores da lista."""
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
valores_cópia = valores[:]
dobra(valores_cópia)
print(valores_cópia)
print(valores)