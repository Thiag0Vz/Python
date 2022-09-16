from statistics import median


def notas(*x):
    '''
    ma = maior nota
    me = menor nota
    data = dicionário para preenchimento dos dados

    O programa funciona da seguinte forma: na linha 18 temos um for, e para cada c 
    nos dados de x, irá verificar se é maior que a maior nota e menor que a menor nota

    em seguida, será acrescentado o campo "total", que se refere ao total de notas cadastradas, que
    equivale ao tamanho de x
    em seguida será acrescentado no dicionário a maior e menor nota, assim como a média,
    que é calculada utilizando a função median em x. 
    Em sequência, o dicionário será criado.  
    
    
    '''
    ma = 0
    me = 0
    data = {}

    for c in x:
        if c > ma:
            ma = c
        if c <= min(x):
            me = c

    data['total'] = len(x)
    data['maior'] = ma
    data['menor'] = me
    data['média'] = median(x)

    print (data)

notas(5.1,1,9,6)

