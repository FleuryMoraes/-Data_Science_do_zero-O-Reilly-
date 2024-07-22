comidas = ["camarao", "porco_frito", "bolo"]
almoço = "porco_frito"
for refeicao in comidas:
    if refeicao == almoço:
        print (f"comerei hoje {refeicao}")
    else:
        print (f"hoje nao comerei {refeicao}")

gols_flamengo = [10,20,30,40]
for gols in gols_flamengo:
    if (gols >= 20 and gols<40):
        print ("python eh uma pombinha")
    else:
        print ("a linguagem C tem um pau enorme")

procurados = ["Manga", "Chulé", "Tuti", "Pitica"]
for foragidos in procurados:
    if foragidos == "Tuti":
        print ("Achamos o suspeito!")
    else:
        print (f"não estamos atrás do(a) {foragidos}...")

#checando se uma lista está ou não vazia
pizza = ["marguerita", "mussarela"]
if pizza:
    print (f"Você deseja uma {pizza[0]} ou uma {pizza[1]}?")
else:
    print ("Não temos pizzas disponíveis")

disponivel = ("sexo_selvagem", "drogas", "anime", "biquinis", "monster_energy", "tetas")
requisitado = ["drogas", "tetas"]
for pedido in requisitado:
    for temos in disponivel:
        if pedido == temos:
            print (f"Claro, hoje temos {temos} no cardapio!")
        else:
            print (f"Você gostaria também de {temos}?")
             

