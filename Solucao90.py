media = float(input())
linhas = []

while True:
    valores = input()
    if valores == 'fim':
        break
    soma = 0
    lista = valores.split()
    for c in lista:
        soma += int(c)
    med = soma / len(lista)
    if med * 2 < media:
        break
    if med > media:
        linhas.append(valores)

for x in linhas:
    print(x)
####
# user: kayck.souza@ccc.ufcg.edu.br
# group: 22.1
# mode: lista5
# open_datetime: 2022-12-19T23:33:24.998429
# create_datetime: 2022-12-19T23:33:24.998429
# revision: 1
# activity: 5843614150164480
# assignment: 4533848970887168
# ip: 2804:7f7:2680:67e7:8512:7171:63f4:5b2f
# timestamp: 2804:7f7:2680:67e7:8512:7171:63f4:5b2f
