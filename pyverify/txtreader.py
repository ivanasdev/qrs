import re 

f = open ('textouno.txt','r')

mensaje = f.read()

items= mensaje.split()


file= open('exploit.txt','w')
for item in items:
    file.write(item+"\n")



#readed= re.search("Identificador", mensaje)
#txt = "Identificador Electrónico"
#x = re.split("\s", txt,1)
#print(readed)
