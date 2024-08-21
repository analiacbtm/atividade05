media_ssp = float(input())
acima_media = []

while True:
    seq = input()
    lista_seq = seq.split()
    soma = 0

    if lista_seq == ['fim']:
        break

    for num in lista_seq:
        soma += int(num)

    media = soma / len(lista_seq)

    if media > media_ssp:
        acima_media.append(seq)

    if media * 2 < media_ssp:
        break

for sequencia in acima_media:
    print(sequencia)
####
# user: hebert.laurentino.santos@ccc.ufcg.edu.br
# group: 22.1
# mode: None
# open_datetime: 2022-12-05T13:17:19.186797
# create_datetime: 2022-12-05T13:17:19.186797
# revision: 2
# activity: 5843614150164480
# assignment: 5263893821652992
# ip: 150.165.42.220
# timestamp: 150.165.42.220
