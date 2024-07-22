#dicionarios sao tal qual o plano cartesiano: para cada x, há um y
cor_olhos = {"Glauco":"marrom", "Diego":"azul", "Pai":"verde escuro", "Mãe":"verde claro"}
print (f"Cor dos seus olhos: {cor_olhos['Glauco']}")
cor_olhos["Pitica"] = "marrom"
cor_olhos["Tuti"] = "verde-acastanhado"
print (cor_olhos)

ideologias = {"Glauco":"socialista", "Diego":"ancap", "Pais":"massa de manobra"}
print (f"Sua ideologia é {ideologias["Glauco"]}")
ideologias["Glauco"] = "Alcoolismo"
print (f"Sua nova ideologia é {ideologias['Glauco']}")

xadrez = {"kanye West": "bode", "Snoop Dogg": 420}
print (xadrez.get ("kanye West", "nao temos o kanye hj =( )"))
print (xadrez.get ("50 cent", "Many men, wish death upon me!"))#meio memes esse 'get' aí
print (xadrez)
del(xadrez["kanye West"])
print (xadrez)

perfil = {"nome": "Glauco", "NUSP": "15456302", "Idade": "19 anos de idade"}
print (perfil.items())
#loop dentro de um dicionário!
for chave, conteudo in perfil.items():
    print (f"chave: {chave}")
    print (f"conteudo: {conteudo}")
musicos = {"kendrick":"how much a dollar cost", "kanye west":"blame game", "the smiths":
           "heaven knows I'm miserable now"}
for musicas in musicos.keys():#tem as funções 'keys' e 'values'
    print (musicas.title())

amigos = ["José", "Purgato", "Pedro", "Kaita", "Li", "Renan"]
gostos = {"José":"funk", "Purgato":"punk", "Pedro":"prog", "Kaita":"rock", "Li":"alt", "Renan":"pop"}
for nomes in amigos:
    print (f"Ola, tudo bem com você {nomes}?")
    for pessoa,musica in gostos.items():
        if pessoa == nomes:
            print (f"Caramba {pessoa}, não sabia que tu curtia {musica}!")
#pra fazer busca em dicionário com alguma ordem em mente,  basta que tu vá lá e aplique a 
#função de organização na parada; ex: 'sorted(gostos.keys())' (retorna em ordem alfabética)

#pra organiar dicionários, temos 3 funções: 'value()', 'key()', e 'item()'
#a função 'set()' desconsidera itens repetidos
cores = ["azul", "roxo", "cinza", "roxo", "verde"]
print (cores)
print (set(cores))

#'nesting' é fazer lista de listas, de dicionários, dicionários de listas, etc.
#lista de dicionarios:
cachorro1 = {"Nome":"Tuti", "Cor":"ruiva", "Porte":"médio"}
cachorro2 = {"Nome":"Pitica", "Cor":"branca&preta", "Porte":"pequeno"}
cachorros = [cachorro1, cachorro2]
for animal in cachorros:
    print (f"Nome = {animal["Nome"]}\nCor = {animal["Cor"]}\nPorte = {animal["Porte"]}")

#dicionario de listas:
caracteristicas = {"nome":"Glauco", "altura":1.86, "cara": ['nariz', 'boca', 'olhos']}
for traços, tipo in caracteristicas.items():
    if (traços == "cara"):
        print ("Quanto ao seu rosto, ele contém:")
        for feições in tipo:
            print (f"\t{feições}")
    else:
        print (f"Seu/sua {traços} é {tipo}")

#dicionário de dicionários! (pq vetor de vetores é a famosa matriz!!!)
segunda = {"manhã":"punhetão", "tarde":"desenhar", "noite":"pensar em putaria"}
terça = {"manhã":"se cagar", "tarde":"programar", "noite":"mexer no pinto mole"}
quarta = {"manhã":"ouvir música", "tarde":"encarar crianças até chorarem", "noite":"joe biden"}
semana = {"dia1":segunda, "dia2":terça, "dia3": quarta}
for dias in semana.values():
    print (f"Toda {dias}, eu faço 3 coisas:")#a solução aqui seria fazer um vetor cm os dias da semana
    for horarios,atividade in dias.items():
        print (f"{horarios}:{atividade}")
