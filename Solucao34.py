mediaSSP = float(input())
listaMaiorMedia = []

while True:
    registroMensal = input()
    if registroMensal == 'fim':
        break

    listaMensal = registroMensal.split(' ')
    listaMensal = [int(e) for e in listaMensal]

    somaMensal = 0
    for e in listaMensal:
        somaMensal += e
    mediaMensal = somaMensal / len(listaMensal)

    if mediaMensal > mediaSSP:
        listaMaiorMedia.append(registroMensal)
    if mediaMensal < mediaSSP / 2:
        break

for e in listaMaiorMedia:
    print(e)
####
# user: diego.souto.maior.aleixo@ccc.ufcg.edu.br
# group: 22.1
# mode: None
# open_datetime: 2022-11-09T00:48:24.678174
# create_datetime: 2022-11-09T00:48:24.678174
# revision: 2
# activity: 5843614150164480
# assignment: 6588110370504704
# ip: 177.37.145.248
# timestamp: 177.37.145.248
