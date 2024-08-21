media_mensal = float(input())

media_maior = ''
while True:
    ocorrencias = input()
    if ocorrencias == 'fim': break
    
    valor = ocorrencias.split()

    i = 0
    soma, media = 0, 0
    while i < len(valor):
        soma += int(valor[i])
        i += 1

    media = soma / len(valor)
    
    if media > media_mensal:
        ocorrencias += '\n'
        media_maior += ocorrencias

    if media < (media_mensal / 2): break


print(media_maior, end='')
####
# user: thales.bruno.barros@ccc.ufcg.edu.br
# group: 21.2
# mode: None
# open_datetime: 2022-07-18T20:55:29.054935
# create_datetime: 2022-07-18T20:55:29.054935
# revision: 1
# activity: 5843614150164480
# assignment: 6337510256934912
# ip: 177.37.146.116
# timestamp: 177.37.146.116
