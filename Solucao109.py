media_estabelecida = float(input())
parada = media_estabelecida / 2

media_alta = []
while True:
    diario = input()
    oco = diario.split()
    if oco == ['fim']: break
    soma = 0
    for i in range(len(oco)):
        oco[i] = int(oco[i])
        soma += oco[i] / len(oco)
    if soma < parada: break
    if soma > media_estabelecida:
        media_alta.append(diario)

for i in media_alta:
    print(f'{i}')


####
# user: lucas.pereira@ccc.ufcg.edu.br
# group: 21.2
# mode: None
# open_datetime: 2022-07-06T23:55:53.722233
# create_datetime: 2022-07-06T23:55:53.722233
# revision: 2
# activity: 5843614150164480
# assignment: 6368848217374720
# ip: 177.73.205.32
# timestamp: 177.73.205.32
