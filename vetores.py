#VETORES: indexação, que nem em C, mas sem o asterisco, pq nn vamos alocar dinamicamente
gatos = ["Miau", "Bebê", "Pussy", "Bruxinha"]
print (gatos[2].upper())
print ("Esses são 2 dos meus gatos:", gatos[1], "e", gatos[0])
print (f"Eu não gosto muito do {gatos[2]}, prefiro o {gatos[3]}!") #precisa do 'f'

princesas = ["Tony Soprano", "Jackie Chan", "Bolsonaro", "Marcelo Manzato"]
print (princesas)
princesas.append ("Maggie Thatcher") 
print (princesas)
princesas.insert (0, "Ovomaltine")
print (princesas)
del princesas[2]
print (princesas)
princesas.remove ("Bolsonaro")
print (princesas)

comida = ["Cogumelos", "Frango frito", "cerâmica", "Cebolinha"]
print (sorted(comida))#ordem alfabética
comida.reverse()#inverte o vetor
print (comida)
print (len(comida))#idêntico ao strlen


