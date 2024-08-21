media_ssp = float(input())
lista = ""

while True:
    soma = 0 

    valores = input().split()

    if valores[0] == 'fim':
        break
    else:
        for valor in valores:
            soma += int(valor)
            media = soma/len(valores)
    
        if media > media_ssp:

            for i in range(len(valores)):
                if i == (len(valores)-1):
                    lista += valores[i] + '\n'
                else:
                    lista += valores[i] + ' ' 


        elif media < (media_ssp/2):
            break

print(lista, end='')
####
# user: carmelita.medeiros@ccc.ufcg.edu.br
# group: 21.2
# mode: None
# open_datetime: 2022-06-17T15:56:28.278262
# create_datetime: 2022-06-17T15:56:28.278262
# revision: 1
# activity: 5843614150164480
# assignment: 5465494305898496
# ip: 177.75.78.66
# timestamp: 177.75.78.66
