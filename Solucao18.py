#Prog1
#Cainan Martins
#Crimes

media = float(input())
total = 0
lista = []

while True:
    entrada = input().split( )

    if entrada == ["fim"]:
        break

    for t in entrada:
        total += float(t)        
    
    calc = total / len(entrada)
    
    if calc < (media/2):
        break

    elif calc > media:
        lista.append(entrada)

    for s in lista:
        resp = ""
        teste = len(resp)

        for h in range(len(s)): 
            if h == len(s)-1:
                resp += h
            
            else:
                resp += h + " "

print (resp)

####
# user: cainan.silva.martins@ccc.ufcg.edu.br
# group: 22.1
# mode: None
# open_datetime: 2022-12-05T13:15:06.073721
# create_datetime: 2022-12-05T13:15:06.073721
# revision: 1
# activity: 5843614150164480
# assignment: 5320648945565696
# ip: 150.165.42.204
# timestamp: 150.165.42.204
