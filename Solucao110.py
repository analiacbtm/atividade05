media = float(input())
saida = []

while True:
    soma = 0
    lista = []
    sequencia = input()

    if sequencia == 'fim': break

    for elemento in sequencia.split():
        num = int(elemento)
        lista.append(num)

    for numero in lista:
        soma += numero
        media_sequencia = soma / len(lista)

    if media_sequencia >= media:
        saida.append(sequencia)

for s in saida:
    print(s)
####
# user: lucas.soares@ccc.ufcg.edu.br
# group: 21.1e
# mode: None
# open_datetime: 2022-02-10T02:02:56.169153
# create_datetime: 2022-02-10T02:02:56.169153
# revision: 1
# activity: 5219602246139904
# assignment: 4601554889867264
# ip: 2804:970:81d0:3800:82f8:5f0f:ae8f:5d7b
# timestamp: 2804:970:81d0:3800:82f8:5f0f:ae8f:5d7b
