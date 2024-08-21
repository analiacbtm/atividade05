media_ssp = float(input())
resultados = []

while True:
    entrada = input()
    lista = entrada.split()

    if entrada == 'fim':
        break

    media = 0
    acumulador = 0
    for i in lista:
        acumulador += int(i)

    media = acumulador / len(lista)
    if media < media_ssp/2:
        break

    if media >= media_ssp:
        resultados.append(entrada)
    
for i in resultados:
    print(i)####
# user: marcos.antonio.pereira@ccc.ufcg.edu.br
# group: 21.2
# mode: None
# open_datetime: 2022-06-20T21:26:53.978023
# create_datetime: 2022-06-20T21:26:53.978023
# revision: 1
# activity: 5843614150164480
# assignment: 4823084353716224
# ip: 2804:29b8:5066:31e2:c02c:f6ae:640b:a25
# timestamp: 2804:29b8:5066:31e2:c02c:f6ae:640b:a25
