media = float(input())
soma = 0
lista_maior = []

while True:
    entrada = input()
    if entrada == "fim":
        break
    valores = entrada.split()
    soma = 0

    for valor in valores:
        soma+= float(valor)
    media_val = soma / len(valores)
    if media_val * 2 < media:
        break
    if media_val > media:
        lista_maior.append(entrada)

for lista in lista_maior:
    print(lista)
####
# user: andreza.farias@ccc.ufcg.edu.br
# group: 22.1
# mode: None
# open_datetime: 2022-11-07T21:06:22.945541
# create_datetime: 2022-11-07T21:06:22.945541
# revision: 1
# activity: 5843614150164480
# assignment: 6697927047118848
# ip: 150.165.42.181
# timestamp: 150.165.42.181
