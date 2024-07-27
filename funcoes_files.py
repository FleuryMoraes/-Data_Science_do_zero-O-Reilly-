#criar funcoes gerais, uma classe de POEMAS, e outra pra LOVECRAFT
from pathlib import Path

def corta_palavra (palavra):
    letras = []
    pontuacao = [';', ':', '.', ':', '!', '?']
    for letra in palavra:
        flag = 0
        for ponto in pontuacao:
            if ponto == letra:
                flag = 1
        if flag == 0:        
            letras.append (letra)    
    return letras

def lista_reversa (lista):
    reversa = [None] * len (lista) #é assim que tu cria uma vazia cm tamanho fella
    posicao = len(lista)-1
    for elemento in lista:
        reversa[posicao] = elemento
        posicao -= 1
    return reversa    

def num_palavras (file):
    palavras = file.split() #quebra em lista de strings, sendo '\t' o critério
    numero = len (palavras) #conta o n° de elementos da lista
    return numero      
    
class Poema (): #permite buscar rimas e a palavra 'amor'
    def __init__(self, file, arquivo):
        self.arquivo = arquivo
        self.file = file
        self.rimas = 0

    def numero_palavras (self):
        quantia = num_palavras (self.file) #bizarro ter que jogar uma função dentro da outra
        return quantia

    def buscar_rimas (self):#bastante simples: 'rima' são 2 palavras que terminam com 2 letras iguais
        #não usar o read_text! Quero o file purinho
        filezinho = open (f"{self.arquivo}", "r") #esse formato me é mais familiar que o uso do Path, e parece ser melhor 
        paridade = 1
        verso = 0
        while True: #tem que tirar o '\n', que vai dar certo
            linha = filezinho.readline()
            verso += 1 
            if not linha: #detecta o EOF
                break
            linha = linha.strip()#remove os whitespaces
            if not linha:#pula linhas vazias (PQ FUNCIONA GPT???)
                continue
            palavras = linha.split()#transformei a string numa lista, xupa federal
            palavras.reverse()   
            if paridade%2 == 1:
                rima1 = palavras[0]
                rima1 = corta_palavra (rima1)
                rima1.reverse()
            else:
                rima2 = palavras[0]
                rima2 = corta_palavra (rima2)
                rima2.reverse()
                if rima1[0]==rima2[0] and rima1[1]==rima2[1]:
                    print (f'Há uma rima no verso {verso}, com as palavras {"".join(lista_reversa(rima1))} e {"".join(lista_reversa(rima2))}.')
            paridade += 1

    def buscar_amor (self):
        palavras = self.file.split()
        count = 1
        flag = False
        for palavra in palavras:
            if palavra == 'amor' or palavra == 'Amor':
                print (f'Achamos "amor" como a {count}° palavra no texto.')
                flag = True
            count += 1
        if flag == False:
            print ("Não achamos 'amor' nesse texto.") 

class Lovecraft (Poema):
    def __init__ (self, file):
        super().__init__(file)
        
    def buscar_amor (self):
        print ('Não há amor nos poemas de H.P Lovecraft.')

    def indescritivel (self):
        classicos = ['indescritível', 'inominável', 'inefável']
        palavras = self.file.split()
        classics = 0
        for palavra in palavras:
            if palavra == classicos[0-2]: #tá certo isso daq?
                classics += 1
        print (f'As palavras "indescritivel", "inominavel", "inefavel" aparecem {classics} vezes.')

                
                




            
