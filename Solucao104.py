media_ssp = float(input())
lista = []
while True:
    sequencia = input()
    ocorrencias = sequencia.split()
    total = 0
    if sequencia == "fim": break
    for num in ocorrencias:
        total += int(num)
    media_mensal = total / len(ocorrencias)
    if media_mensal <= media_ssp / 2: break
    if media_mensal > media_ssp:
        lista.append(sequencia)

for s in range(len(lista)):
    print(lista[s])
####
# user: lucas.correia@ccc.ufcg.edu.br
# group: 21.1e
# mode: None
# open_datetime: 2022-03-06T16:43:15.059553
# create_datetime: 2022-03-06T16:43:15.059553
# revision: 1
# activity: 5219602246139904
# assignment: 5808955391475712
# ip: 2804:29b8:50c0:fce:e6ba:6f69:e929:a28e
# timestamp: 2804:29b8:50c0:fce:e6ba:6f69:e929:a28e
