media_prevista = float(input())
superou = []
while True:
    ocorrencias = input()
    if ocorrencias == 'fim':
        break
    lista = ocorrencias.split()

    soma = 0
    media = 0
    for e in lista:
        soma += int(e)
    media = soma / len(lista)

    if media <= media_prevista / 2:
        break
    elif media > media_prevista:
        superou.append(lista)

for elemento in superou:
    saida = ''
    for j in range(len(elemento) - 1):
        saida += elemento[j] + ' '
    saida += elemento[-1]
    print(saida)
####
# user: ana.rita.medeiros.souza@ccc.ufcg.edu.br
# group: 22.1
# mode: None
# open_datetime: 2022-11-11T21:21:55.509188
# create_datetime: 2022-11-11T21:21:55.509188
# revision: 2
# activity: 5843614150164480
# assignment: 5623273146548224
# ip: 2804:29b8:5066:87fb:859a:3759:abbb:d906
# timestamp: 2804:29b8:5066:87fb:859a:3759:abbb:d906
