#P1 -UFCG
# Criminalidade
# seleciona meses em que a média de ocorrências por dia > média da (ssp)
# ou para de ler quando a entrda receber uma 2 vezes menor (/2) que a media ssp.

mean_ssp = float(input())
while True:
    seq_media_month = input()
    if seq_media_month == 'fim':
        break

    valor_media_month = seq_media_month.split()
    i = 0
    soma = 0
    while True:
        if i >= len(valor_media_month):
            break
        soma += int(valor_media_month[i])
        i += 1
    mean = float(soma / len(valor_media_month))
    if mean < mean_ssp / 2:
        break
    if mean > mean_ssp:
        print(seq_media_month)


####
# user: jamilly.silva@ccc.ufcg.edu.br
# group: 21.2
# mode: None
# open_datetime: 2022-06-29T18:56:36.821877
# create_datetime: 2022-06-29T18:56:36.821877
# revision: 3
# activity: 5843614150164480
# assignment: 6302213779488768
# ip: 2804:29b8:505e:faa4:a7fc:96e2:5658:b53d
# timestamp: 2804:29b8:505e:faa4:a7fc:96e2:5658:b53d
