#o objetivo com esse codigo é ler os arquivos que tu quiser e aplicar um monte de coisas neles
#NÃO admite files binários
import funcoes_files as funcoes

print ('Esse programa apenas lê arquivos no formato txt.')
print ("Digite 'fim' quando não tiver mais arquivos para análise.")
print ("Escreva aqui CORRETAMENTE o nome do(s) arquivo(s):")
count = 1
success = False
while True: #NAO ESQUEÇA DE FECHAR O FILE
    arquivo = input (f'{count}° arquivo: ')
    if arquivo == 'fim':
        break
    else: 
        try: 
            file = open (f"{arquivo}", "r")#não está funcionando =(
            success = True
        except FileNotFoundError:
            print ("Você não digitou o arquivo corretamente!")
            success = False     
    if success == True:
        count += 1
        texto = file.read()
        print ('Escreva "fim" se quiser mudar de file;')
        poem = input('É um poema? (S = sim / N = não) ')
        hp = input('É do HP Lovecraft? (S = sim / N = não) ')
        print ('Escreva "count" se quiser saber quantas palavras tem o texto;')
        if (poem == 'S'):
            texto = funcoes.Poema (texto, arquivo)
            print ('Escreva "amor" para printar quantas vezes a palavra aparece; ')
            print ('Escreva "rimas" para saber as rimas que aparecem; ')
            if (hp == 'S'):
                texto = funcoes.Lovecraft (texto)
                print ('Escreva "indescritivel" para saber quão cafona tá o hp;')    
        comando = ''
        while comando != "fim":
            comando = input("Escreva seu comando: ")
            if comando == 'count':
                if poem == 'N':
                    total = funcoes.num_palavras (texto) 
                else:
                    total = texto.numero_palavras()    
                print (f'Há {total} palavras no texto.')
            if comando == 'amor':
                texto.buscar_amor()
            if comando == 'rimas':
                texto.buscar_rimas()
            if comando == 'indescritivel':
                texto.indescritivel()
file.close()
     
            