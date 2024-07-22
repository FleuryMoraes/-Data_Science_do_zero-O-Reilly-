#FUNÇÃO INPUT
nome = input ("digite seu nome: ")
print (f"Esse é seu nome: {nome}")
#se tu quiser usar numero, tem que 'desestringzar' eles"
idade = input("digite sua idade: ")
print (f"Essa é sua idade: {idade}")
idade = int(idade)
idade += 3
print (f"Daqui a 3 anos, você terá {idade} anos!")
#o operador de 'modulo' tambem retorna o resto da divisao pra voce
idade = idade % 2
print (f"Se cada ano valesse 1/2 ano, você teria {idade}")#isso tá errado kakaak