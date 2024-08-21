media_ssp = float(input())

acima_da_media = []

while True:
    soma_ocorrencias = 0

    ocorrencias = input()
    if ocorrencias == 'fim': break

    ocorrencias = list(ocorrencias.split())
    for n in range(len(ocorrencias)):
        ocorrencias[n] = int(ocorrencias[n])
        soma_ocorrencias += ocorrencias[n]

    media_diaria = soma_ocorrencias / len(ocorrencias)

    if (media_diaria * 2) < media_ssp: break

    if media_diaria > media_ssp:
        acima_da_media.append(ocorrencias)

for e in range(len(acima_da_media)):
    saida = ''
    saida2 = ''
    for i in range(len(acima_da_media[e])):
        saida += str(acima_da_media[e][i]) + ' '
    for s in range(len(saida) - 1):
        saida2 += saida[s]
    print(saida2)
####
# user: carlos.henriche.goncalves@ccc.ufcg.edu.br
# group: 21.2
# mode: None
# open_datetime: 2022-06-21T01:40:21.539195
# create_datetime: 2022-06-21T01:40:21.539195
# revision: 3
# activity: 5843614150164480
# assignment: 6260607374327808
# ip: 187.183.198.4
# timestamp: 187.183.198.4
