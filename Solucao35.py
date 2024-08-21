def calcula_media(sequencia):
    soma = 0

    for valor in sequencia:
        soma += int(valor)

    return soma / len(sequencia)


media_mensal = float(input())

acima_media = []
while True:
    sequencia = input()

    if sequencia == 'fim': break

    media_seq = calcula_media(sequencia.split())

    if media_seq < (media_mensal / 2): break

    elif media_seq > media_mensal:
        acima_media.append(sequencia)

for item in acima_media:
    print(item)
####
# user: douglas.domingos.silva@ccc.ufcg.edu.br
# group: 22.1
# mode: None
# open_datetime: 2022-11-09T13:59:05.311728
# create_datetime: 2022-11-09T13:59:05.311728
# revision: 1
# activity: 5843614150164480
# assignment: 6517624118706176
# ip: 177.86.181.190
# timestamp: 177.86.181.190
