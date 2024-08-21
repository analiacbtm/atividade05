# Universidade Federal de Campina Grande - UFCG
# Ciência da Computação
# Rafael Araújo dos Santos (121210335)
# Exercício Unidade 5 - Acima da média (Criminalidade)

media_ssp = float(input())
seq = ""
soma = 0
numeros = 0

while True:
    seq = input()

    if seq == "fim":
        break;

    valores = seq

    for n in range(len(valores.split())):
        numeros = valores.split()
        soma = soma + int(numeros[n])

    media = soma / len(valores.split())

    if media < (media_ssp / 2):
        break
    elif media > media_ssp:
        seq_maior = seq
        print(seq_maior)
    soma = 0 # Zera a soma dos valores da seq, usados para calcular a média
####
# user: rafael.araujo.santos@ccc.ufcg.edu.br
# group: 21.2
# mode: None
# open_datetime: 2022-06-17T18:00:02.210503
# create_datetime: 2022-06-17T18:00:02.210503
# revision: 1
# activity: 5843614150164480
# assignment: 5858771576291328
# ip: 177.73.204.140
# timestamp: 177.73.204.140
