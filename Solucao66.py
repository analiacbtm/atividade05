ssp = float(input())
entrada = []
numeros = []
saida = []

while True:
    entrada = input()
    if entrada == "fim": break
    else:
        soma = 0
        numeros = entrada.split()
        for i in range(0, len(numeros)):
            soma += int(numeros[i])
        media = soma/(len(numeros))
        if media < ssp/2 : break
        if media > ssp:
            saida.append(entrada)
       
for linha in saida:
    print(linha)
####
# user: hennan.heim.falcao@ccc.ufcg.edu.br
# group: 22.1
# mode: None
# open_datetime: 2022-11-29T17:36:47.639571
# create_datetime: 2022-11-29T17:36:47.639571
# revision: 1
# activity: 5843614150164480
# assignment: 6385529983598592
# ip: 2804:29b8:5059:37:4acb:45cc:a873:b949
# timestamp: 2804:29b8:5059:37:4acb:45cc:a873:b949
