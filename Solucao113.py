media_ssp = float(input())
sequencia = ""

soma = 0
media = 0
sequencias = []

while True:
    sequencia = input()
    if sequencia == "fim":
        break
    sequencia = sequencia.split()
    for elemento in sequencia:
        soma += int(elemento)
    media = soma/len(sequencia)
    if media <= media_ssp/2:
        break
    elif media > media_ssp:
        sequencias.append(sequencia)
    soma = 0
    media = 0

saida = ""

for x in range(0, len(sequencias)):
    for indice in range(0, len(sequencias[x])):
        if indice == len(sequencias[x])-1:
            saida += f"{sequencias[x][indice]}"
        else:
            saida += f"{sequencias[x][indice]} "
    print(saida)
    saida = ""
####
# user: marcos.antonio.albuquerque.santos@ccc.ufcg.edu.br
# group: 22.1
# mode: None
# open_datetime: 2022-11-13T21:18:28.302545
# create_datetime: 2022-11-13T21:18:28.302545
# revision: 1
# activity: 5843614150164480
# assignment: 6355898668679168
# ip: 177.73.202.132
# timestamp: 177.73.202.132
