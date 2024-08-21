mediassp = float(input())
l1 = []
maiores = []

while True:
    entrada = input().split()
    if entrada == ["fim"]:
        break
    else:
        soma = 0
        for i in entrada:
            soma+=int(i)
        mediareal = soma/(len(entrada))

        if mediareal > mediassp:
            maiores.append(entrada)

        elif mediareal < (mediassp/2):
            break

if len(maiores) > 0:
    for j in range(len(maiores)):
        print(*maiores[j])####
# user: rodrigo.nascimento@ccc.ufcg.edu.br
# group: 22.1
# mode: None
# open_datetime: 2022-11-23T16:53:11.686186
# create_datetime: 2022-11-23T16:53:11.686186
# revision: 1
# activity: 5843614150164480
# assignment: 5760760737169408
# ip: 150.165.74.96
# timestamp: 150.165.74.96
