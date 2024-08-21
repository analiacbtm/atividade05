media = float(input())
media_minima = media / 2
soma = 0
lista_numeros = []
while True:
    numero = input()
    if numero == 'fim':
        break
    numeros = numero.split()
    for i in range(len(numeros)):
        if int(numeros[i]) != 0:
            soma += int(numeros[i])
    media_numeros = soma / (len(numeros))
    if media_numeros > media:
        lista_numeros.append(numero)
    if media_numeros < media_minima:
        break
    soma = 0
for item in lista_numeros:
    print(item)
####
# user: lucas.ariel.carvalho@ccc.ufcg.edu.br
# group: 21.2
# mode: None
# open_datetime: 2022-08-06T21:28:03.325877
# create_datetime: 2022-08-06T21:28:03.325877
# revision: 1
# activity: 5843614150164480
# assignment: 6218148283940864
# ip: 177.37.146.195
# timestamp: 177.37.146.195
