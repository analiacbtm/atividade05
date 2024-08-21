def exibe(lista):
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            if j == len(lista[i]) - 1:
                print(lista[i][j])
            else:
                print(lista[i][j], end=' ')

def calcula_media(lista):
    media = 0
    for e in lista:
        media += int(e)

    return media/len(lista)

media = float(input())
acima = []

while True:
    entrada = input().split()

    if entrada[0] == 'fim' or calcula_media(entrada) < (media / 2):
        break

    if calcula_media(entrada) > media:
        acima.append(entrada)

exibe(acima)

####
# user: leandro.oliveira.souto@ccc.ufcg.edu.br
# group: 22.1
# mode: None
# open_datetime: 2022-12-01T01:06:33.428632
# create_datetime: 2022-12-01T01:06:33.428632
# revision: 2
# activity: 5843614150164480
# assignment: 6717919515901952
# ip: 177.73.205.112
# timestamp: 177.73.205.112
