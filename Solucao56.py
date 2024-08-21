mediaL = float(input())
lista = []
def contem(valor, lista):
    status = False
    for i in range(len(lista)):
        if lista[i] == valor:
            status = True
    return status
def join(separador,lista):
    saida = ''
    for i in range(len(lista)):
        saida += lista[i]
        if i == len(lista) - 1:
            break
        saida += separador
    return saida
while True:
    entrada = input().split()
    soma = 0
    if contem('fim',entrada):
        break
    for i in range(len(entrada)):
            soma += int(entrada[i])
    if (soma / len(entrada)) > mediaL:
        lista.append(entrada)
    elif (soma / int(len(entrada))) < (mediaL / 2):
        break
for i in range(len(lista)):
    lista1 = lista[i]
    print(join(' ',lista1))####
# user: gabriel.souza@ccc.ufcg.edu.br
# group: 21.2
# mode: None
# open_datetime: 2022-06-21T13:41:42.905114
# create_datetime: 2022-06-21T13:41:42.905114
# revision: 1
# activity: 5843614150164480
# assignment: 5984415207391232
# ip: 45.191.254.227
# timestamp: 45.191.254.227
