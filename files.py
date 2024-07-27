#FILES: pra trabalhar com files no python, tem que importar a biblioteca 'pathlib', expecificamente
#usando a classe 'Path' e jogando como argumento pra ela o nome do teu file.
#o Python busca files na mesma pasta que o programa está rodando, sendo ṕssível usar paths 'relativos' 
#(pastas dentro da atual) ou 'absolutos' (pastas externas) para indicar pro Python onde buscar o(s) file(s)
#funções da classe Path: 'readtext()','splitlines()', 'write_text()' (se quiser guardar numero, tem que
#converter em string com str() ) + (se nao existir o file, cria ele; se existir, apaga o conteúdo), 
from pathlib import Path

arquivo = input ("Digite EXATAMENTE o file que tu quer ler: ")
try:
    path = Path (f'{arquivo}')
except FileNotFoundError:
    print ("Você não digitou o arquivo do Camões corretamente!")    
poema = path.read_text()
versos = poema.splitlines()
for linha in versos:
    if 'Amor' in linha:
        linha = linha.replace ('Amor', 'Tesão')
    print (linha)

#EXCEÇÕES: python gera objectos desse tipo quando dá caca: aí você pode usar blocos do tipo 'try-except',
#em que, se 'try' não funciona, ele procura um 'except' que contenha o erro relatado e executa oq tem lá.
#formato: 'try-except-else'. Se quiser que o programa falhe, mas continue operando sem reclamar, faça: 
#'try: -comando- except: pass
#NOTA: na parte dos files, dá pra você salvar eles usando os comandos json.dumps() e json.loads(); só usar 'import json';
#pra receber input do usuario e lembrar, basta usar um TRY-EXCEPT com o json


