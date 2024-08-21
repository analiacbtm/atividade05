media_estabelecida = float(input())
saida = list()

medias_mensais = list()
while True:
    medias_mensais = input().split()
    if medias_mensais[0] in 'fim':
        break
    else:
        soma = 0
        contador = 0
        for i in range(len(medias_mensais)):
            soma += int(medias_mensais[i])
            contador +=1
        media = soma / contador
        if media > media_estabelecida:
            saida.append(medias_mensais)
        elif media <= media_estabelecida / 2:
            break
for i in range(len(saida)):
    for j in range(len(saida[i])):
        if j == len(saida[i]) - 1:
            print(saida[i][j])
        else:
            print(saida[i][j], end=' ')

####
# user: anny.caroline.alves.silva@ccc.ufcg.edu.br
# group: 22.1
# mode: None
# open_datetime: 2022-11-09T13:12:32.087844
# create_datetime: 2022-11-09T13:12:32.087844
# revision: 1
# activity: 5843614150164480
# assignment: 6031469757595648
# ip: 45.229.175.186
# timestamp: 45.229.175.186
