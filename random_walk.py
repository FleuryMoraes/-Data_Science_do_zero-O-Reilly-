import matplotlib.pylab as plt
from random import choice

class RandomWalk:
    def __init__(self, pontos = 5000):
        self.pontos = pontos
        self.valor_x = [0]
        self.valor_y = [0]

    def walk (self):
        while (len(self.valor_x) < self.pontos):
            #direção e intensidade do vetor deslocamento
            direcao_x = choice ([-1,1])
            distancia_x = choice ([0,1,2,3,4])
            caminhada_x = direcao_x * distancia_x
            direcao_y = choice ([-1,1])
            distancia_y = choice ([0,1,2,3,4])
            caminhada_y = direcao_y * distancia_y
            if caminhada_y == 0 or caminhada_x == 0:
                continue
            #adicionar mudanças ao status atual
            x = self.valor_x[-1] + caminhada_x
            y = self.valor_y[-1] + caminhada_y
            #atualizar a situação da partícula
            self.valor_x.append (x)
            self.valor_y.append (y)

while (True):
    rw = RandomWalk ()
    rw.walk ()
    #plotando o gráfico
    plt.style.use ('dark_background')
    fig, ax = plt.subplots(figsize=(12, 7)) #mexer na 'fig' aumenta a imagem exposta
    ax.scatter(rw.valor_x, rw.valor_y, c=rw.valor_y,cmap=plt.cm.Blues, s=15)
    ax.set_aspect('equal')
    plt.show()
    #gerar mais random_walks!!
    stop = input ("Pressione enter para prosseguir, e escreva 'pare' para o halt: ")
    if stop == '':
        continue
    else:
        break