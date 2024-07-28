#TINHA QUE MUDAR O INTERPRETADOR; ainda tá uma bosta, mas faz o L né mano, já perdi umas 3h nessa desgraça 
#(ele por algum motivo ainda não identifica o matplot.lib às vezes)
import matplotlib.pyplot as plt
plt.style.use ("Solarize_Light2")
#o módulo 'pyplot' basicamente tem um monte de função que ajuda a plotar gráfico
#se quiser customizar mais os gráficos, vai no terminal e digita (noo python): 'import matplotlib.pyplot as plt' + 'plt.style.available'
#e digite 'plt.style.use('estilo_que_tu_quiser')' antes de chamar a 'subplots()'
def graf_1():
    dominio = [1,2,3,4,5,6,7,8,9,10]
    imagem = [1,2,3,4,5,6,7,8,9,10] #reta afim (y=x)

    fig, ax = plt.subplots() #fig representa todos os plots, e ax, um individual
    ax.scatter (2, 2, s=200)
    ax.plot (dominio, imagem, linewidth = 5) #plota o bagulho
    ax.set_title("Reta afim", fontsize=24)
    ax.set_xlabel("Domínio", fontsize=14)
    ax.set_ylabel("Imagem", fontsize=14)
    ax.tick_params(labelsize=12)

    plt.show() #mostra no matplotlib oq rolou

def graf_2():
    pontos_x = [0,1,2,3,4,5]
    porntos_y = [0,1,4,9,16,25] #parábola (y=x²)

    fig, ax = plt.subplots()
    ax.scatter (pontos_x, porntos_y, s=100)#vai fazer um gráfico só de pontinhos
    ax.set_title("Parábola", fontsize=24)
    ax.set_xlabel("Domínio", fontsize=14)
    ax.set_ylabel("Imagem", fontsize=14)
    ax.tick_params(labelsize=12)

    plt.show() 

def graf_3():
    pontos_x = range (1,1001)
    pontos_y = [x**2 for x in pontos_x] #parábola mais definida

    fig, ax = plt.subplots()
    ax.scatter(pontos_x, pontos_y,color = (0,0.8,0), s=10) #como são mtos dados, reduzimos o tamanho de cada ponto pra s=10
    ax.set_title("Parábola definida", fontsize=24)
    ax.set_xlabel("Domínio", fontsize=14)
    ax.set_ylabel("Imagem", fontsize=14)
    ax.axis([0, 1100, 0, 1_100_000])#define o tamanho máximo e minimo dos 2 eixos, resp. x e y

    plt.show()
    #pra numeros imensos, usa notação científica (se quise manter padrão: 'ax.ticklabel_format(style='plain')'
    #pra mudar a cor dos pontos, entre 'pontos_x' e 'pontos_y' em scatter, escreva color='cor_que_quiser'(entre aspas mesmo)) ou use RGB
    #dá pra fazer gradientes gráficos usando o 'colormap';  tem que ver os específicos na biblioteca do matlib
    #pra salvar figuras, use 'plt.savefig()' no lugar de 'plt.show()'






      


