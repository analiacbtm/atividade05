media_mensal_secre = float(input())

nova = []
while True:
    ocorrencia_diaria = input()
    if ocorrencia_diaria == "fim":
        for elemento in nova:
            print(elemento)
        break

    ocorrencia_separada = ocorrencia_diaria.split()

    soma = 0
    for ocorrencia in range(len(ocorrencia_separada)):
        soma += int(ocorrencia_separada[ocorrencia])

    media = float(soma/len(ocorrencia_separada))

    if media > media_mensal_secre:
        nova.append(ocorrencia_diaria)

    if media < (media_mensal_secre/2):
        for elemento in nova:
            print(elemento)
        break
####
# user: rian.melo@ccc.ufcg.edu.br
# group: 21.2
# mode: None
# open_datetime: 2022-07-19T22:30:15.938616
# create_datetime: 2022-07-19T22:30:15.938616
# revision: 2
# activity: 5843614150164480
# assignment: 5829377239547904
# ip: 2804:26d8:301:8e:1512:1084:aa1e:809
# timestamp: 2804:26d8:301:8e:1512:1084:aa1e:809
