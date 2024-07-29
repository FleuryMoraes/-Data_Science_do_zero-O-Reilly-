#auxílios importantes: bibliotecas importadas, tal qual IPython, matplotlib, collections, random, re (mexer cm strings),mypy (erros de tipagem)
#digitar IPython no terminal pra usar (%paste e outros comandos úteis)
#usar conjuntos no lugar de listas e dicionários também é uma boa às vezes (trabalhar com diagrama de Venn)
import matplotlib.pyplot as plt
import csv
import json

#plotagem de temperaturas no 'vale da morte'
def vale_da_morte ():
    print ('Certifique-se de que possua esse arquivo no seu PC antes, disponível no github do livro Python Crash Course, cap.17.')
    comando = input('Pressione "enter" para prosseguir, e escreva algo caso não deseje isso: ')
    if comando == '':
        try:
            file = open ('death_valley_2014.csv')
        except:
            print ('Algo deu errado; tente novamente') 
        maxT = []
        minT = [] 
        conteudo = csv.reader (file, delimiter = ',') #o arquivo separa tudo por vírgulas, então tu tem que usar elas p/delimitar
        header = next (conteudo) #importante! pula o header
        for linha in conteudo:
            if linha[1] != "":
                maxT.append ((float(linha[1])-32)*(5/9)) #conversão pra celsius
                minT.append ((float(linha[2])-32)*(5/9))
        meanT = [(x+y)/2 for x, y in zip(maxT, minT)] #testando um jeito de operar com as listas
        xs = [i for i,_ in enumerate(maxT)] #dá a base pro nosso gráfico
        plt.plot (xs, maxT, 'g-', label = 'temperatura máxima')
        plt.plot (xs, minT, '-r.', label = 'temperatura mínima')#(NOTA->pra q servem essas letrinhas?)
        plt.plot (xs, meanT, 'b:', label = 'temperatura média')
        plt.legend (loc=9)#'loc-9' = topo-centro; cria  a legenda cm os labels
        plt.xlabel ('dias do ano') #podia usar tbm o plt.axis pra melhorar a visualização se pá
        plt.ylabel ('temperatura em °C')
        plt.xticks (rotation = 30) #inclina as labels nas abcissas, pra ficar mais fofinho
        plt.title ('Temperaturas com o passar dos dias no "Death-Valley", CA')
        plt.show ()

#plotagem de populacao em regiões do mundo, de 1960 a 2010 (os dados do pyhton tão ruins, NAO USAR!)
def populacao ():
    print ('Certifique-se de que possua esse arquivo no seu PC antes, disponível no github do livro Python Crash Course, cap.17.')
    comando = input('Pressione "enter" para prosseguir, e escreva algo caso não deseje isso: ')
    if comando == '':
        try:
            file = open ('population_data.json')
        except:
            print ('Algo deu errado; tente novamente')
    dados = json.load (file) #cria um dicionário pra buscar no file
    pais = []
    pop = []
    for objetos in dados:
        if objetos["Year"] == '2010': #só vou usar os dados de 2010
            pais.append (objetos["Country Name"])
            pop.append (float(objetos["Value"])) #lê como string, mas eu quero usar como número
    plt.figure(figsize=(10, 6))         
    plt.bar (range (len (pais)), pop) #(NOTA: acho q está errado :/) (COMO MUDAR O TAMANHO DISSO???)
    plt.title ("População nas áreas do mundo em 2010")
    plt.ylabel ("população (milhões de habitantes)")
    plt.xticks (range (len (pais)), pais, rotation = 90)
    plt.tight_layout() #adapta o gráfico à tela do pc
    plt.show ()

print ('Digite "vale" para ver as temperaturas no vale da morte, na Califórnia.')
print ('Digite "mundo" para ver a população humana pelo planeta em 2010.')
entrada = input('entrada: ')
if entrada == 'vale':
    vale_da_morte ()
if entrada == 'mundo':
    populacao ()    

        

            
