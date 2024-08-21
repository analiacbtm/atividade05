media_ssp = float(input())
quebra = media_ssp / 2
while True:
    sequencia = input()
    if sequencia == 'fim': break
    soma = 0
    lista = sequencia.split()
    for valor in lista:
        soma += int(valor)
    media = soma / len(lista)
    if media < quebra: break
    if media > media_ssp:
        print(sequencia)
####
# user: iasmim.maria.torres@ccc.ufcg.edu.br
# group: 21.1e
# mode: None
# open_datetime: 2022-02-16T19:51:32.114524
# create_datetime: 2022-02-16T19:51:32.114524
# revision: 2
# activity: 5219602246139904
# assignment: 5705240420548608
# ip: 177.86.181.243
# timestamp: 177.86.181.243
