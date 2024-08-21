#coding: utf-8
#p1 - UFCG - 13 de fevereiro de 2022
#Miguel de Oliveira Rodrigues - 121110343
#Imprime os meses onde a média de ocorrências seja maior que a estabelecida.

media_maxima = float(input())

lista_valores = []
medias = []
while True:
    valores = input()
    
    soma = 0
    if valores == "fim": break
    for valor in valores.split():
        soma += int(valor)

    media = soma / len(valores.split())
    if media <= media_maxima / 2: break
    
    lista_valores.append(valores)
    medias.append(media)


for i in range(len(lista_valores)):    
    if medias[i] > media_maxima:
        print(lista_valores[i])

####
# user: miguel.rodrigues@ccc.ufcg.edu.br
# group: 21.1e
# mode: None
# open_datetime: 2022-02-13T21:04:00.008254
# create_datetime: 2022-02-13T21:04:00.008254
# revision: 5
# activity: 5219602246139904
# assignment: 5881361694982144
# ip: 138.94.50.161
# timestamp: 138.94.50.161
