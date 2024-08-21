#Questão Acima da Média Vinícius Teixeira de Melo Lopes 09/11/2022

mssp = float(input())
lista = []
soma = 0
while True:
    valores = input()
    if valores == 'fim':
        break
    else:
        separados = list(valores.split())
        for n in separados:
            soma += int(n)
        if (soma/len(separados)) > mssp:
            lista.append(valores)
        if (soma/len(separados)) < (mssp/2):
            break
        soma = 0
for item in lista:
    print(item)



####
# user: vinicius.teixeira.melo.lopes@ccc.ufcg.edu.br
# group: 22.1
# mode: None
# open_datetime: 2022-11-09T23:14:59.643244
# create_datetime: 2022-11-09T23:14:59.643244
# revision: 1
# activity: 5843614150164480
# assignment: 6202232456347648
# ip: 45.228.145.145
# timestamp: 45.228.145.145
