#iniciamos funções com 'def', e usamos tal qual no C
#podemos usar 'keyboard_arguments' (pra dar match mais fácil) e estabelecer argumentos default
def descricao (nome, profissao, idade):
    if (nome) == "":
        nome = 'Zé-Ninguém'
    if (profissao) == "":
        profissao = 'vagabundo'
    if (idade) == "":
        idade = '21'        
    print (f"Meu nome eh {nome}, eu sou um(uma) {profissao} profissional, e tenho {idade} anos")
    idade = int(idade)
    idade += 50
    return idade

print ("Se tu não quiser responder algo, só pressione 'enter")
nome = input ("Qual teu nome? ")
profissao = input ("Em que tu trampa? ")
idade = input ("Há quantos anos tu tá aqui? ")
novo = descricao(nome, profissao, idade)
print (f'daqui a 50 anos, você terá {novo} seu troxa!')

#uma função pode receber, modificar, e alterar quaisquer funções que tu passar pra ela: basta tratar o 
#argumento já assumindo como sendo um desses, no 1° caso
#podemos passar um numeros N de argumentos desse modo: 'def mod(*pessoas)'; o python criará uma 
#tupla pra armazenar esses valores; o mesmo pode ocorrer para um dicionários, com 'def pin(**nome_e_nusp)'
def boletim (nome, *reprovacoes, **extras):
    print (f'Pois bem, senhor {nome}, vejamos seu boletim! Quantas vezes tu reprovou?')
    print (f'Reprovaste {len(reprovacoes)} vezes, com as seguintes notas:')
    for notas in reprovacoes:
        print (f'-{notas}')
    print ('Vejamos agora o que anotaram extra de ti;')
    count = 1
    for dia, ocorrido in extras.items():
        print (f'{count}° burrada: {dia} você foi lá e {ocorrido}')
        count += 1

nome = input("Digite o nome do azarado: ")
reprovacoes = []
print ('Digite as notas das reprovações,teclando fim quando chegarem ao fim:')
notas = ''
while notas != 'fim':
    notas =  input ()
    if notas != 'fim':
        reprovacoes.append (int (notas))#fazendo cm que printe 2 ao invés de '2'
extras = {}
print ('Agora fale das ocorrencias, na ordem data + ocorrido, seguindo o comando fim já estabelecido;')
while True:
    data = input ("data: ")
    if data == 'fim':
        break
    ocorrido = input("ocorrido: ")
    extras[data]  = ocorrido
boletim (nome, *reprovacoes, **extras)#tem que passar o argumento com o asterisco '*', senão não entende

#tu pode criar bibliotecas pra ti mesmo importar, é só colocar tudo num mesmo diretório;
#tbm dá pra importar uma função específica, e mudar o nome ('from module_name import function_name as fn')
#pra importar TODAS as funções de um módulo, taca um asteriscozinho no finalzinho ('import bib*')
