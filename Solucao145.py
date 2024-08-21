media_mensal = float(input())
medias = []

while True:
    ocorrencias = input()
    list_ocorrencias = ocorrencias.split()

    if list_ocorrencias[0] == 'fim':
        break

    soma = 0
    for n in list_ocorrencias:
        soma += int(n)
    media = soma / len(list_ocorrencias)

    if media > media_mensal:
        medias.append(ocorrencias)

    if media * 2 < media_mensal:
        break

for ocorrencia in medias:
    print(ocorrencia)
####
# user: samuel.lucas.vieira.matos@ccc.ufcg.edu.br
# group: 22.1
# mode: None
# open_datetime: 2022-11-07T17:15:45.316950
# create_datetime: 2022-11-07T17:15:45.316950
# revision: 1
# activity: 5843614150164480
# assignment: 6397900965806080
# ip: 187.19.131.199
# timestamp: 187.19.131.199
