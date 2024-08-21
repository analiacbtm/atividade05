elementosmaiormedia = []
elementos = ''
mediainformada = float(input())
mediacalculada = 0
somaelementos = 0

while True:
    valores = input()
    if valores == "fim":
        break
    elementos = valores.split(" ")
    
    somaelementos = 0
    for k in range(0,len(elementos)):
        somaelementos += int(elementos[k])
    mediacalculada = somaelementos / len(elementos)

    if mediacalculada * 2 < mediainformada:
        break

    if mediacalculada > mediainformada:
        elementosmaiormedia.append(valores)
        
    
for d in elementosmaiormedia:
    print(d)






    




         

####
# user: aline.brito.maracaja@ccc.ufcg.edu.br
# group: 22.1
# mode: None
# open_datetime: 2022-11-10T20:13:02.638581
# create_datetime: 2022-11-10T20:13:02.638581
# revision: 3
# activity: 5843614150164480
# assignment: 6166763744002048
# ip: 187.19.219.32
# timestamp: 187.19.219.32
