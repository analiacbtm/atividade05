media_spp = float(input())

lista = []
while True:
    entrada = input()
    valores = entrada.split()

    if entrada == 'fim':
        break

    for i in range(len(valores)):  # convertendo de str para int
        valores[i] = int(valores[i])

    soma = 0
    for valor in valores:  # somando cada valor da lista
        soma += valor

    media_valores = soma / len(valores)

    if media_valores > media_spp:  # cada elemento da lista será a sequência de valores
        lista.append(entrada)      # da entrada maiores que a média

    if media_valores < (media_spp / 2):
        break

for elemento in lista:
    print(elemento)
####
# user: vinicius.barbosa@ccc.ufcg.edu.br
# group: 21.2
# mode: None
# open_datetime: 2022-07-04T22:40:36.082856
# create_datetime: 2022-07-04T22:40:36.082856
# revision: 2
# activity: 5843614150164480
# assignment: 5599745940652032
# ip: 2804:29b8:5066:bb58:2271:5a59:7b34:9e47
# timestamp: 2804:29b8:5066:bb58:2271:5a59:7b34:9e47
