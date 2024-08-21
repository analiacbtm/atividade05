"""
PROG1 - UFCG
Caio Jhonatan Alves Pereira
"""

media_estabelecida = float(input())

ocorrencias_por_dia = list()

while True:
    quanti_ocorrencias = input()
    
    if quanti_ocorrencias == "fim": break

    i = 0
    soma_elementos = 0
    while len(quanti_ocorrencias.split()) > i:
        soma_elementos += float(quanti_ocorrencias.split()[i])
        i += 1

    media = soma_elementos / len(quanti_ocorrencias.split())
    
    if media > media_estabelecida:
        ocorrencias_por_dia.append(quanti_ocorrencias)


elementos_imprimir = list()

k = 0
while len(ocorrencias_por_dia) > k:
    print(ocorrencias_por_dia[k])
    k += 1
####
# user: caio.jhonatan.pereira@ccc.ufcg.edu.br
# group: 21.1e
# mode: None
# open_datetime: 2022-02-17T15:34:02.424985
# create_datetime: 2022-02-17T15:34:02.424985
# revision: 1
# activity: 5219602246139904
# assignment: 4966367935594496
# ip: 177.223.53.125
# timestamp: 177.223.53.125
