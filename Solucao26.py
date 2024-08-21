ssp = float(input())

while True:
    lista = []
    entrada = input()
    valores = entrada.split()
    if valores[0] == 'fim':
        break
    v = 0
    for i in valores:
        v += int(i)
    media = v / len(valores)
    if media > ssp:
        print(entrada)
    elif media * 2 < ssp:
        break
   
####
# user: daniella.dantas@ccc.ufcg.edu.br
# group: 21.1e
# mode: None
# open_datetime: 2022-02-11T20:37:06.188864
# create_datetime: 2022-02-11T20:37:06.188864
# revision: 2
# activity: 5219602246139904
# assignment: 5875336258519040
# ip: 177.73.204.9
# timestamp: 177.73.204.9
