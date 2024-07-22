#TESTANDO STRINGS
#testando 'methods' (funções que especificam ao python como lidar com variaveis)
texto = "Glauco Fleury Corrêa de Moraes"
print (texto.title())
print (texto.upper())
print (texto.lower())
#podemos criar tbm 'f-strings', que juntam coisas
texto1 = "Bom Dia"
texto2 = "meu Brasil varonil!"
texto_final = f"{texto1} {texto2}"
print (texto_final)
#whitespace continua igual, com os '\t' e '\n' da vida; os metodos 'rstrip() e lstrip() retiram
#o espacinho pra voce
nome = "Jô Soares "
print (nome.rstrip())
nome = nome.rstrip() #mudei *permanentemente* o bagulho
print (nome) 
titulo = "Sir Isaac Newton"
print (titulo.removeprefix("Sir ")) #tirei o comecinho
print (titulo.removesuffix(" Isaac Newton")) #tirei o finalzinho

#TESTANDO NÚMEROS
x, y, z = 10, 12, 14
ALTURA = 1,86 #boa pratica -> indicar constantes cm upper_case (python nn tem tipagem pra elas)
print (ALTURA)
