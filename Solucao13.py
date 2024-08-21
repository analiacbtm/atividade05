media_ssp = float(input())

while True:
    seq = input()
    list_seq = seq.split()

    if list_seq[0] == "fim":
        break
    soma = 0
    qtd = 0
    for x in list_seq:
        qtd += 1
        soma += int(x)
    
    media = soma/qtd
    if media > media_ssp:
        print(seq)
    elif media <= (media_ssp / 2):
        break
####
# user: anna.beatriz.furtado@ccc.ufcg.edu.br
# group: 21.2
# mode: None
# open_datetime: 2022-07-04T13:28:19.282621
# create_datetime: 2022-07-04T13:28:19.282621
# revision: 1
# activity: 5843614150164480
# assignment: 6626095552004096
# ip: 177.37.144.130
# timestamp: 177.37.144.130
