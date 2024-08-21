media_mensal = float(input())
menor_negado = media_mensal/2
while True:
    ocorrencia = input()
    if ocorrencia == 'fim':
        break
    lista=ocorrencia.split()
    somam=0
    for n in range(len(lista)):
        somam += int(lista[n])
        media_dia=somam/len(lista)
    if media_dia < menor_negado:
        break
    if media_dia > media_mensal:
       print(ocorrencia)####
# user: levi.assuncao@ccc.ufcg.edu.br
# group: 21.2
# mode: None
# open_datetime: 2022-07-12T23:17:36.761720
# create_datetime: 2022-07-12T23:17:36.761720
# revision: 2
# activity: 5843614150164480
# assignment: 4575919354150912
# ip: 177.37.145.122
# timestamp: 177.37.145.122
