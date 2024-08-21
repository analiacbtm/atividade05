def str_to_int_list(string):
    lista = string.split()
    for i in range(len(lista)):
        lista[i] = int(lista[i])
    return lista

def media_entrada(lista):
    soma = 0
    for n in lista:
        soma += n
    media = soma / len(lista)
    return media

limite = float(input())

acima_limite = []
while True:
    dias = input()
    if dias == 'fim':
        for s in acima_limite:
            print(s)
        break

    dias_l = str_to_int_list(dias)
    media = media_entrada(dias_l)

    if media < (limite / 2):
        for s in acima_limite:
            print(s)
        break
    elif media > limite:
        acima_limite.append(dias)
####
# user: vinicius.albuquerque@ccc.ufcg.edu.br
# group: 21.2
# mode: None
# open_datetime: 2022-06-19T00:21:18.809953
# create_datetime: 2022-06-19T00:21:18.809953
# revision: 1
# activity: 5843614150164480
# assignment: 5971102067064832
# ip: 2804:29b8:505d:dc3:c5c7:c410:feb0:dd91
# timestamp: 2804:29b8:505d:dc3:c5c7:c410:feb0:dd91
