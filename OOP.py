#OOP = 'object oriented programming': você cria classes que, se aplicadas a N objetos, farão com que todos
#tenham as mesmas características em comum; criar um objeto de uma classe é 'instanciá-lo'
#é convencional começar uma classe com letra maiúscula
#pense em classes como 'instruções' para criar uma instanciação
#funções em classes são chamadas de métodos, e inicializadas do seguinte modo: '__function__()'; atencão
#aos dois underscores antes e depois do nome da função
#'atributos' são específicos do instanciado ('self.name = name')
#tu pode usar os métodos da classe na instância e também usar seus argumentos específicos
#para mudar um atributo, há 3 maneiras: mudar na instância, usar um método, ou incrementar o valor
class Pessoa:
    def __init__(self, altura, idade, nome):
        self.altura = altura
        self.idade = idade
        self.nome = nome
        self.tempo_juntos = 0
    
    def chamado (self):
        comentario = (f'Bom dia {self.nome}, você tem {self.idade} anos e {self.altura} metros.')
        return comentario
    
    def amizade (self):
        print (f'Nos conhecemos fazem exatos {self.tempo_juntos} anos.')

    def up_amizade (self):
        mod = input ('voces se conhecem faz quanto tempo agora?')
        self.tempo_juntos += int(mod)

#HERANÇA: criação de uma nova classe, que herda métodos e atributos da classe mãe, que deve aparecer antes
#da classe filha no file;
#dá pra redefinir funções na classe filha, que terão prioridade sobre a mãe
#COMPOSIÇÃO: separar hierarquicamente as classes, tal qual na vida real
class Broxice:
    def __init__(self, broxada = 'sinistra'):
        self.broxada = broxada

    def pinto_molisse (self):
        grau = input ("Quão broxa tu acha que um imbecil que nem você é?")
        grau = int(grau)
        grau += 2
        if grau<4:
            self.broxada = 'triste'
        print (f'Tu na real tem uma broxada do tipo {self.broxada}, num grau de {grau}')

class Imbecil (Pessoa):
    def __init__(self, altura, idade, nome):
        super().__init__(altura, idade, nome)
        self.grau_rude = 10
        self.broxa = Broxice()
    
    def burrice (self):
        idiotice = input ("Quão burro você é, de 5-10: ")
        idiotice = int (idiotice)
        self.grau_rude += idiotice
        print (f'Fazendo as contas, tu é um sólido {self.grau_rude} na escala de burrice mano.')

    def chamado (self):
        print ("Não se chama um imbecil!!!")

comando = ''
while comando != 'pare':
    nome= input ("Qual o nome da pessoa? ")
    altura= input ("Qual a altura da pessoa? ")
    idade= input ("Qual a idade da pessoa? ")
    crivo = input ('É ou não uma imbecil? Responda com sim ou não apenas: ')
    if crivo == 'nao':
        nova_pessoa = Pessoa (altura, idade, nome)
        nova_pessoa.chamado()
        nova_pessoa.up_amizade()
        nova_pessoa.amizade()
    else:
        nova_pessoa = Imbecil(altura, idade, nome)
        nova_pessoa.broxa.pinto_molisse()
        nova_pessoa.chamado()
        nova_pessoa.up_amizade()
        nova_pessoa.amizade()
    comando = input ('Digite pare ou pressione enter para prosseguir: ')

#É possível (e encorajado) você importar classes, tal qual com as funções, na forma de módulos, e efetuar
#as mesmas manipulações de antes (importar só uma classe, algumas classes, usar 'aliases', etc.)


    



           
