media_mensal = float(input())
resp = []

while True:
    valor = input()
    if valor == 'fim': break
    valorsplit = valor.split()
    
    soma = 0
    for e in valorsplit:
        soma += int(e)
    media = soma / len(valorsplit)
    
    if media < media_mensal / 2: break

    if media > media_mensal:
        print(valor)
####
# user: leila.medeiros.farias@ccc.ufcg.edu.br
# group: 22.1
# mode: lista5
# open_datetime: 2022-12-20T17:55:05.564761
# create_datetime: 2022-12-20T17:55:05.564761
# revision: 1
# activity: 5843614150164480
# assignment: 4839708490203136
# ip: 177.37.145.55
# timestamp: 177.37.145.55
