# UFCG - Prog1 e Lab de Prog1 - 2022
# Gabriel Erik Silva Nunes - 121110201
# gabriel.erik.nunes@ccc.ufcg.edu.br
# Questão Acima da média

media_mensal_ssp = float(input())

seq_maiores_que_limite = []
while True:
    entrada = input()
    if entrada == 'fim': break
    
    seq = entrada.split()
    soma_mensal = 0
    for num in seq:
        soma_mensal += int(num)

    if len(seq) > 0:
        media_mensal = soma_mensal / len(seq)
    else:
        media_mensal = 0

    if media_mensal > media_mensal_ssp:
        seq_maiores_que_limite.append(seq)

    if media_mensal < media_mensal_ssp / 2: break

for seq in seq_maiores_que_limite:
    concatena_seq = ''
    for num in seq:
        concatena_seq = concatena_seq + num + ' '
    
    print(concatena_seq.strip())
####
# user: gabriel.erik.nunes@ccc.ufcg.edu.br
# group: 21.1e
# mode: None
# open_datetime: 2022-02-09T23:05:20.665041
# create_datetime: 2022-02-09T23:05:20.665041
# revision: 3
# activity: 5219602246139904
# assignment: 5340651216437248
# ip: 177.37.144.36
# timestamp: 177.37.144.36
