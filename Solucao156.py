media = float(input())
sequencias_maiores = list()

while True:
    entrada = input()
    if entrada == 'fim':break
    entrada = entrada.split()

    soma_entrada = 0
    for valor in entrada:
        soma_entrada += int(valor)

    media_entrada = soma_entrada/len(entrada)

    if media > 2*media_entrada: break

    if media_entrada > media:
        sequencias_maiores.append(entrada)

for sequencia in sequencias_maiores:
    sequencia_str = ' '.join(sequencia)
    print(sequencia_str)
####
# user: victor.vinicius.araujo@ccc.ufcg.edu.br
# group: 21.1e
# mode: None
# open_datetime: 2022-02-16T12:39:36.593544
# create_datetime: 2022-02-16T12:39:36.593544
# revision: 2
# activity: 5219602246139904
# assignment: 5804084227473408
# ip: 191.35.81.150
# timestamp: 191.35.81.150
