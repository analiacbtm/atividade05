# Programação I / Laboratório de Programação I - UFCG
# Jônatas Tavares dos Santos - 121110769
# Acima da Média (Unidade 5)

media_ssp = float(input())
valores, medias = [], []
while True:
    entrada = input()
    if (entrada == "fim"): break
    valores.append([int(i) for i in entrada.split()])
    soma = 0
    for i in range(len(valores[-1])):
        soma += valores[-1][i]
    media = soma / len(valores[-1])
    medias.append(media)
    if (media * 2) < media_ssp: break

for i in range(len(medias)):
    if medias[i] > media_ssp:
        for j in range(len(valores[i]) - 1):
            print(valores[i][j], end=" ")
        print(valores[i][j + 1])

####
# user: jonatas.santos@ccc.ufcg.edu.br
# group: 21.1e
# mode: None
# open_datetime: 2022-02-13T21:47:43.793075
# create_datetime: 2022-02-13T21:47:43.793075
# revision: 1
# activity: 5219602246139904
# assignment: 5873714807701504
# ip: 45.170.181.48
# timestamp: 45.170.181.48
