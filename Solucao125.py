media = float(input())

while True:
    entrada = input()
    if entrada == 'fim':
        break
    soma = 0 
    numeros = entrada.split()
    for n in numeros:
        soma += int(n)
    med = soma / len(numeros)
    if med * 2 < media:
        break
    if med > media:
        print(entrada)
####
# user: naiara.medeiros.costa.almeida@ccc.ufcg.edu.br
# group: 22.1
# mode: None
# open_datetime: 2022-11-27T16:59:39.370285
# create_datetime: 2022-11-27T16:59:39.370285
# revision: 1
# activity: 5843614150164480
# assignment: 6378896272392192
# ip: 177.37.144.143
# timestamp: 177.37.144.143
