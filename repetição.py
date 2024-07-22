numeros = [10, 90, 69, 420]
for numero in numeros:
    print (numero)
dias_da_semana = ["segunda", "terça", "quarta", "quinta"]
for numero in numeros:
    print (f"Eu fumei {numero} baseados essa semana")

for i in range (10,13):
    print (i)
numeros_pares = list(range(0,11,2))#o terceiro argumento define um 'adicionador'
#cria uma lista com qqr coisa que tu der
print (numeros_pares)

quadrados = []
for numero in range (1,11):
    quadrados.append (numero**2)
print (quadrados)
print (f"minimo entre os quadrados: {min(quadrados)}")
print (f"maximo entre os quadrados: {max(quadrados)}")

cubos = [valor**3 for valor in range(1,4)]
print (f"cubos de 1, 2, 3: {cubos}")

#pra cortar uma string em pedaços, usamos o vocabulário de 'range' pra strings
str = ["Dedo", "Lingua", "Cu", "e Buceta"]
str1 = str[:2]
str2 = str[-2:]
print (f"Str1: {str1}\nStr2: {str2}")
str_copy = str[:]
print (str_copy)#copia a original

#TUPLAS: vetores imutáveis; usar o '()' ao invés do '[]'
#loop de while
limite = input ("Digite o quanto tu quer que o loop rode: ")
limite = int(limite)
numero = 0
while numero <= limite:
    print (numero)
    numero += 1

texto = ("\nDiga algo para eu repetir para você!")
texto += ("\nEscreva 'caneca' para sair do loop")
mensagem  = ""
while mensagem != "caneca":
    print (texto)
    mensagem = input ()
    print (mensagem)#repare que o input descarta o texto anterior, tal qual o printf
#as 'flags' novamente nos ajudam a decidir o momento do halt

flag = True
while flag:
    numero = input ("Numero (escreva '10' para sair): ")
    numero = int(numero)
    if numero == 10:
        flag = False
#o comando 'break' também está disponível nessa linguagem
