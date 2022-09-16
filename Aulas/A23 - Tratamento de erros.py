#Comandos try, except, else e finally (else e finally são opcionais)
#Tente e se não
#Dentro de try, colocamos a operação que desejamos realizar.
#Caso não seja possível realizar a operação, entra em ação o comando except.
#No comando except, é o que acontece quando há a falha. Caso não haja falha, o except não entra e, ação
#O else é caso o try dê certo.
#O finally vai acontecer independente se der certo ou der errado.

#Também podemos mostrar o tipo de erro, atribuindo a classe principal Exception a uma variável e exibindo-a, em except
from time import sleep
try:
    a = int(input('Digite um número: '))
    b = int(input('Digite um número: '))
    x = a/b #Aqui temos x. Caso apague essa linha, o comando except entra em ação.
    print (f'O valor digitado foi {x}')

except Exception as erro: #O except é tipo: "Se der problema, faz isso". Aqui, o 'Exception as erro' serve pra atribuir o Exception à variável erro, dessa forma mostrando o problema
    print (f'Erro "{erro}" de classe {erro.__class__}')

else:
    print ('O programa funcionou sem erros')

finally:
    sleep(1)
    print ()
    print ('Encerrando')

#Todo try pode ter mais de um except. Podemos atribuir um tipo de erro
#para cada except, e cada except pode ter mais de um tipo de erro, por exemplo:

#except (ValueError, TypeError):
    #print ('Erro no tipo de dado inserido')
#except (ZeroDivisionError):
    #print ('Não é possível dividir por zero')

