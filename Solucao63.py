# Guilherme Dantas Boia de Albuquerque
# Média de criminalidade

ocorrencias = float(input())
limite = ocorrencias / 2

maiores = []

while True:
    entrada = input()
    if entrada == "fim": break

    numeros = [int(num) for num in entrada.split()]
    soma = 0
    for num in numeros:
        soma += num

    media = soma / len(numeros)
    if media < limite: break
    if media > ocorrencias:
        maiores.append(entrada)

for elemento in maiores:
    print(elemento)
####
# user: guilherme.dantas.boia.albuquerque@ccc.ufcg.edu.br
# group: 22.1
# mode: None
# open_datetime: 2022-11-08T18:48:05.210363
# create_datetime: 2022-11-08T18:48:05.210363
# revision: 3
# activity: 5843614150164480
# assignment: 6659179731222528
# ip: 177.37.144.132
# timestamp: 177.37.144.132
