#UFCG
#ana.fernandes - turma 21.2
#solução Acima da média (Criminalidade)

media_dept = float(input())
soma = 0
lista_maior = []

while True:
    entrada = input()
    if entrada == 'fim': break
    valores = entrada.split()
    soma = 0
    for valor in valores:
        soma += float(valor)

    media_valores = soma / len(valores)

    if media_valores * 2 < media_dept: break

    if media_valores > media_dept:
        lista_maior.append(entrada)

for lista in lista_maior:
    print(lista)
####
# user: ana.fernandes@ccc.ufcg.edu.br
# group: 21.2
# mode: None
# open_datetime: 2022-08-08T14:22:16.994892
# create_datetime: 2022-08-08T14:22:16.994892
# revision: 1
# activity: 5843614150164480
# assignment: 4675860558774272
# ip: 177.37.146.223
# timestamp: 177.37.146.223
