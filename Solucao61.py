# Computação | UFCG
# Programação I | 2021.1
# Geyson Maik | 121110138 | 16/02/2022
# Acima da média: Determinar as sequências que tem média acima do normal. 

media_ssp = float(input())

acima =  []
while True:
    sequencia = input()
    if sequencia == "fim": break
    soma = 0
    for i in sequencia.split():
        soma += int(i)
    media = soma / len(sequencia.split()) 
    if media < media_ssp / 2: break
    if media > media_ssp:
        acima.append(sequencia)

for i in acima:
    print(i)
####
# user: geyson.maik.carvalho@ccc.ufcg.edu.br
# group: 21.1e
# mode: None
# open_datetime: 2022-02-15T21:51:34.813345
# create_datetime: 2022-02-15T21:51:34.813345
# revision: 1
# activity: 5219602246139904
# assignment: 5797430282944512
# ip: 168.0.233.244
# timestamp: 168.0.233.244
