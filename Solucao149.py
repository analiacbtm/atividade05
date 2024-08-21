media = float(input())
lista = []

while True:
    entrada = input().split()
    
    if entrada[0] == 'fim': break
    entrada = [int(i) for i in entrada]


    if (sum(entrada) / len(entrada)) > media: 
        lista.append(entrada)

    if (sum(entrada) / len(entrada)) < (media / 2): break


for j in lista:
    saida = ''
    for x in range(len(j)):
        if x!= len(j)-1:
            saida += str(j[x]) + ' '
        if x == len(j)-1:
            saida += str(j[x])
    print(saida)
    
####
# user: suelen.felix@ccc.ufcg.edu.br
# group: 21.2
# mode: None
# open_datetime: 2022-06-18T23:27:13.875393
# create_datetime: 2022-06-18T23:27:13.875393
# revision: 1
# activity: 5843614150164480
# assignment: 6573078173712384
# ip: 177.10.201.63
# timestamp: 177.10.201.63
