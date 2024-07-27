#baixando no seu pc a biblioteca 'pytest', você pode criar códigos que testam seus demais códigos
#a ferramenta 'pip' em python permite baixar essas bibliotecas externas que já não vvem embutidas com o programa: o nome do file
#de teste DEVE começar com 'test', chamando a função a ser testada com argumentos bolados e usando o 'assert'
#só digitar 'pytest' no terminal =)

from fonte import corta_palavra as cp
from fonte import lista_reversa as ls

def test_cp ():
    #a função efetivamente corta as palavras?
    teste = cp ('mamão')
    assert teste == ['m','a','m','ã','o']
    teste = cp ('m!e!u;D,e.u!s!')
    assert teste == ['m','e','u','D','e','u','s']

def test_ls ():
    #a função consegue inverter listas?
    teste = ls ([1,2,3,4,5])
    assert teste == [5,4,3,2,1]
    teste = ls (['a','m','o','r'])
    assert teste == ['r','o','m','a']    