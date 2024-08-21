md_mensal = float(input())
lista = []
x = ''
while True:
    lista2 = []
    soma = 0
    valor = input()
    if valor == "fim":
        break
    lista.append(valor.split())
    lista2.append(valor.split())
    for x in range(len(lista2[0])):
        soma += int(lista2[0][x])
    if (soma / len(lista[0])) < md_mensal / 2:
        break

for y in range(len(lista)):
    soma = 0
    media = 0
    for z in range(len(lista[y])):
        soma += int(lista[y][z])
    media = soma/len(lista[y])
    if media > md_mensal:
        x = " ".join(lista[y])
        print(x)

####
# user: luan.rodrigues@ccc.ufcg.edu.br
# group: 21.2
# mode: None
# open_datetime: 2022-06-17T16:09:45.830447
# create_datetime: 2022-06-17T16:09:45.830447
# revision: 2
# activity: 5843614150164480
# assignment: 5245293865992192
# ip: 2804:29b8:505e:dfc:714c:6a8c:fc14:fea1
# timestamp: 2804:29b8:505e:dfc:714c:6a8c:fc14:fea1
