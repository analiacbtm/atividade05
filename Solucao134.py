def calcula_media(lista):
    soma = 0
    tamanho = len(lista)
    for i in range(tamanho):
        soma += int(lista[i])
    media = soma / tamanho
    return media


mssp = float(input())
valores = []
while True:
    numeros = input()
    ocorrencias = numeros.split()

    if ocorrencias == ['fim']: break

    else:
        media = calcula_media(ocorrencias)
        if media > mssp:
            valores.append(numeros)
        elif media * 2 < mssp:
            break
for lista in valores:
    print(lista)



####
# user: pedro.pereira@ccc.ufcg.edu.br
# group: 21.2
# mode: None
# open_datetime: 2022-06-16T12:23:18.608054
# create_datetime: 2022-06-16T12:23:18.608054
# revision: 2
# activity: 5843614150164480
# assignment: 6467750828441600
# ip: 2804:29b8:505a:83dc:91ff:dee3:de07:bb87
# timestamp: 2804:29b8:505a:83dc:91ff:dee3:de07:bb87
