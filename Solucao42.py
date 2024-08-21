# UFCG - P1
# Aluno: Evaldo Alves de Brito Júnior
# matrícula: 121110090
# Atividade: Acima da média (Criminalidade)

media_ssp = float(input())

sequencia = ""
lista = []
soma = 0
divisor = 0
media_dias = 0
saida = []
while True:
    sequencia = input()
    if sequencia == "fim": break
    lista = sequencia.split()
    #media da sequencia
    for n in lista:
        n = int(n)
        soma += n
        divisor += 1
    media_dias = soma / divisor
    #saida
    if media_dias <= (media_ssp / 2): break
    if media_dias > media_ssp:
        saida += [sequencia]
    #reload
    soma = 0
    divisor = 0

for e in saida:
    print(e)
####
# user: evaldo.brito.junior@ccc.ufcg.edu.br
# group: 21.1e
# mode: None
# open_datetime: 2022-02-16T23:54:38.446521
# create_datetime: 2022-02-16T23:54:38.446521
# revision: 1
# activity: 5219602246139904
# assignment: 6360805337464832
# ip: 45.191.253.20
# timestamp: 45.191.253.20
