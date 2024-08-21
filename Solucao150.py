# UFCG ~ PROG1
# TAWAN BARBOSA DA SILVA | 120211073
# Acima da média | u5

media_ssp = float(input())
acimamedia = []

while True:
    entrada = input()
    
    if entrada == "fim":
        break

    ocorrencias = entrada.split()
    valores = 0

    for i in range(len(ocorrencias)):
        valores += int(ocorrencias[i])
    
    media = valores / len(ocorrencias)
    
    if media > media_ssp:
        acimamedia.append(entrada)
    
    if media * 2 < media_ssp:
        break

for i in range(len(acimamedia)):
    print(acimamedia[i])

####
# user: tawan.silva@ccc.ufcg.edu.br
# group: 21.1e
# mode: None
# open_datetime: 2022-03-06T11:25:14.890543
# create_datetime: 2022-03-06T11:25:14.890543
# revision: 1
# activity: 5219602246139904
# assignment: 5341108496236544
# ip: 168.181.227.135
# timestamp: 168.181.227.135
