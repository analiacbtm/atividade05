#UFCG - Curso Ciência da Computação - 2021.2 - Laboratório de Programação I
#karyna.araujo@ccc.ufcg.edu.br - 121210171
#programa deve imprimir na saída apenas as sequências cuja média mensal é maior que o estabelecido.

media_mensal = float(input())
valores_validos = []
media = 0
while True:
    valores = input()

    if valores == 'fim':
        break

    lista = list(valores.split(' '))
    soma = 0

    for numero in lista:
        soma += int(numero)

    media = soma / len(lista)

    if media > media_mensal:
        valores_validos.append(valores)

    if media < (media_mensal / 2):
        break

for item in valores_validos:
    print(item)

####
# user: karyna.araujo@ccc.ufcg.edu.br
# group: 21.2
# mode: None
# open_datetime: None
# create_datetime: 2022-07-27T23:32:53.268234
# revision: 2
# activity: 5843614150164480
# assignment: 5484011470192640
# ip: 177.37.147.102
# timestamp: 177.37.147.102
