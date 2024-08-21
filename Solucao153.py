media_ssp = float(input())
resposta = []
while True:
    soma = 0
    valores = input().split()

    if valores[0] == "fim": break

    for x in valores:
        soma += int(x)
    media = soma/len(valores)

    if media >  media_ssp:
        for x in valores:
            resposta.append(x)
        resposta.append("pula linha")

    elif 2 * media < media_ssp: break

for x in range(len(resposta) - 1):
    if resposta[x+1] == "pula linha":
        print(f"{resposta[x]}")
    elif resposta[x] != "pula linha":
        print(f"{resposta[x]}", end = " ")
####
# user: victor.carneiro.santos.angelo@ccc.ufcg.edu.br
# group: 22.1
# mode: None
# open_datetime: 2022-11-07T19:37:24.214808
# create_datetime: 2022-11-07T19:37:24.214808
# revision: 1
# activity: 5843614150164480
# assignment: 5342409934241792
# ip: 2804:29b8:505a:1c20:b226:82b2:15c9:3e15
# timestamp: 2804:29b8:505a:1c20:b226:82b2:15c9:3e15
