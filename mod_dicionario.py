conhecido = {}
flag = True
while flag:
    print ("digite 'fim' para terminar o programa, e 'mod' para modificar uma posição;")
    print ("Digite o nome da pessoa e se é amigo ou cuzao: ")
    nome = input ()
    if nome == 'fim':
        break
    else:
        if nome == 'mod':
            suspeito = input ("Qual conhecido quer mudar?")
            for nome, status in conhecido.items():
                novo_nome = input ("Digite o nome da nova pessoa: ")
                conhecido[novo_nome] = conhecido.pop(suspeito)#usamos o 'pop' pra mudar a key
                novo_status = input ("Digite agora o status dessa nova pessoa: ")
                conhecido[novo_nome] = novo_status
                break
        else:
            situation = input ()
            conhecido[nome] = situation            
print (conhecido)