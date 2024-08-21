#Media estabelecida
media_estab = float(input())

# Media dia > media estabelicida, se isso ocorrer duas vezes = break

maior = 0

while True:
    saida = ''
    media_dia = input().split()

    if media_dia == ["fim"]: break
    valores = 0
    cont = 0

    # percorrendo elementos
    for c in media_dia:
        valores += int(c)
        cont += 1

    # Média 
    media = valores // cont

    #verificando se é maior
    if media < media_estab/2:
        break

    if media > media_estab:
        i = 0
        while i < len(media_dia):
            if i == len(media_dia) -1:
                saida += f'{media_dia[i]}'
            else:
                saida += f'{media_dia[i]} ' 
            i += 1
        print(saida)



####
# user: ronaldd.feliph.matias.costa@ccc.ufcg.edu.br
# group: 22.1
# mode: None
# open_datetime: 2022-11-28T21:01:25.098973
# create_datetime: 2022-11-28T21:01:25.098973
# revision: 3
# activity: 5843614150164480
# assignment: 5834627329556480
# ip: 150.165.42.186
# timestamp: 150.165.42.186
