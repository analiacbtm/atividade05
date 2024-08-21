media_limite = float(input())

saida = []
while True:
    entrada = input()
    if entrada == 'fim':
        break

    lista = entrada.split()
    soma = 0
    for num in lista:
        soma += int(num)
    media_mes = soma/len(lista)

    if (media_mes * 2) < media_limite:
        break
    elif media_mes > media_limite:
        saida.append(entrada)

for mes in saida:
    print(mes)
####
# user: moab.alves.silva@ccc.ufcg.edu.br
# group: 22.1
# mode: None
# open_datetime: 2022-11-09T21:18:13.396477
# create_datetime: 2022-11-09T21:18:13.396477
# revision: 1
# activity: 5843614150164480
# assignment: 5409433905528832
# ip: 45.181.138.162
# timestamp: 45.181.138.162
