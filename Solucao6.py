# UFCG
# Programação 1  Turma: 2022.1
# ana.fernandes@ccc.ufcg.edu.br
# Solução para <https://p1ufcg.github.io/#/as/5385238274375680>

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
# group: 22.1
# mode: None
# open_datetime: 2022-11-16T22:54:11.808378
# create_datetime: 2022-11-16T22:54:11.808378
# revision: 2
# activity: 5843614150164480
# assignment: 5385238274375680
# ip: 177.37.144.239
# timestamp: 177.37.144.239
