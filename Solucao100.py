def calcula_media(numeros):
    lista_entrada = numeros.split()
    soma = 0

    for num in lista_entrada:
        soma += int(num)

    return soma / len(lista_entrada)

media_ssp = float(input())

while True:
    entrada = input()
    if (entrada == 'fim'): break

    media = calcula_media(entrada)

    if media_ssp < media:
        print(entrada)
    if media < (media_ssp / 2): break
####
# user: livia.buriti@ccc.ufcg.edu.br
# group: 21.1e
# mode: None
# open_datetime: 2022-03-18T20:41:46.478455
# create_datetime: 2022-03-18T20:41:46.478455
# revision: 1
# activity: 5219602246139904
# assignment: 5863585899085824
# ip: 2804:29b8:5059:2d77:afbf:1171:3581:23b0
# timestamp: 2804:29b8:5059:2d77:afbf:1171:3581:23b0
