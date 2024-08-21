media_ssp = float(input())

while True:
    valores = input()
    lista_valores = valores.split()

    if lista_valores[0] == "fim":
        break

    soma = 0
    quant = 0
    for x in lista_valores:
        soma += int(x)
        quant += 1

    media = soma/quant
    if media > media_ssp:
        print(valores)
    elif media <= (media_ssp / 2):
        break
####
# user: luana.leite@ccc.ufcg.edu.br
# group: 21.2
# mode: None
# open_datetime: 2022-07-04T13:28:24.182272
# create_datetime: 2022-07-04T13:28:24.182272
# revision: 1
# activity: 5843614150164480
# assignment: 4518643482230784
# ip: 45.229.174.59
# timestamp: 45.229.174.59
