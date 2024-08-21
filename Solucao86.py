media = float(input())
resultado = ""
listaFrase = []

while True:
    entrada = input().split()
    if entrada[0] == "fim": break

    soma = 0
    for num in entrada:
        soma += int(num)

    media_entrada = soma / len(entrada)

    if media_entrada < media / 2: break

    if media_entrada > media:
        for i in range(len(entrada)):
            if i == len(entrada) - 1:
                resultado += entrada[i]
            else:
                resultado += entrada[i] + " "
        listaFrase.append(resultado)
        resultado = ""

for frase in listaFrase:
    print(frase)

####
# user: jose.arthur.bezerra@ccc.ufcg.edu.br
# group: 21.1e
# mode: None
# open_datetime: 2022-02-13T20:39:21.665828
# create_datetime: 2022-02-13T20:39:21.665828
# revision: 1
# activity: 5219602246139904
# assignment: 4982090166697984
# ip: 177.73.205.142
# timestamp: 177.73.205.142
