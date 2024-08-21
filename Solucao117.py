media_mensal = float(input())
lista = ""

while True:
    soma = 0
    cont = 0
    sequencia = input()
    if (sequencia == "fim"): break
    for num in sequencia.split():
        soma += int(num)
        cont += 1
    media = soma / cont
    if media <= (media_mensal / 2): break
    if media > media_mensal:
        lista += sequencia + ";"

for sequencia in lista.split(";"):
    if sequencia != "":
        print(sequencia)
        
####
# user: maria.eduarda.farias@ccc.ufcg.edu.br
# group: 21.1e
# mode: None
# open_datetime: 2022-03-09T21:25:30.606169
# create_datetime: 2022-03-09T21:25:30.606169
# revision: 1
# activity: 5219602246139904
# assignment: 5060492244549632
# ip: 191.253.18.157
# timestamp: 191.253.18.157
