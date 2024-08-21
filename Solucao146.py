limite = float(input())
acimamedia = []
while True:
    soma=0
    numeros = input()
    if numeros == "fim":break
    listanumero = numeros.split()
    for numero in listanumero:
        soma+=int(numero)
    media = soma/(len(listanumero))
    if media <= (limite/2): break
    if media > limite:
        acimamedia.append(numeros)
for elemento in acimamedia:
    print(elemento)
####
# user: samuel.luna@ccc.ufcg.edu.br
# group: 21.2
# mode: None
# open_datetime: 2022-07-06T15:56:21.602358
# create_datetime: 2022-07-06T15:56:21.602358
# revision: 1
# activity: 5843614150164480
# assignment: 6414563849273344
# ip: 2804:29b8:505a:7713:44f0:dfaa:cd48:597e
# timestamp: 2804:29b8:505a:7713:44f0:dfaa:cd48:597e
