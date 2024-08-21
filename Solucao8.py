# Universidade Federal de Campina Grande
# Programação 1
# Ana Beatriz Cavalcanti dos Santos
# Programa que lê a média mensal estabelecida pela secretaria de segurança pública e várias sequencias de valores que representam a quantidade de ocorrências registradas por dia na delegacia e imprime na saída apenas as sequências cuja média mensal é maior que o estabelecido.

limite = float(input())


def media_ocorrencias():
    soma = 0
    media = 0
    for i in range(len(ocorrencias_split)):
        ocorrencias_split[i] = int(ocorrencias_split[i])
        soma += ocorrencias_split[i]

    media += soma/len(ocorrencias_split)
    return media


saida = []
while True:
    ocorrencias = input()
    if ocorrencias == "fim":
        break

    ocorrencias_split = ocorrencias.split()
    media = media_ocorrencias()
    if media > limite:
        saida.append(ocorrencias)

    if media < limite / 2:
        break
for i in range(len(saida)):
    print(f"{saida[i]}")
####
# user: ana.santos@ccc.ufcg.edu.br
# group: 21.2
# mode: None
# open_datetime: 2022-06-29T00:02:58.442302
# create_datetime: 2022-06-29T00:02:58.442302
# revision: 3
# activity: 5843614150164480
# assignment: 5774775907516416
# ip: 177.10.202.198
# timestamp: 177.10.202.198
