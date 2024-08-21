media_ssp = float(input())
medias_maiores = []

while True:
    linha = input()
    if linha == 'fim':
        break

    media = 0
    valores = linha.split()
    for v in valores:
        media += int(v)
    media = media / len(valores)

    if media > media_ssp:
        medias_maiores.append(linha)
    elif media <= media_ssp / 2:
        break

for m in medias_maiores:
    print(m)
####
# user: luisa.ledra.azevedo@ccc.ufcg.edu.br
# group: 22.1
# mode: None
# open_datetime: 2022-11-07T15:27:31.405847
# create_datetime: 2022-11-07T15:27:31.405847
# revision: 1
# activity: 5843614150164480
# assignment: 6367302746374144
# ip: 2804:29b8:505a:42cf:8c5f:baad:aec0:3ee7
# timestamp: 2804:29b8:505a:42cf:8c5f:baad:aec0:3ee7
