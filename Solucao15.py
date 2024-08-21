mediaSecretaria = float(input())

continua = True
linhasMaiores = []

while continua:
    crimesPorDia = input('')
    if crimesPorDia == 'fim':
        continua = False
        break

    crimes = crimesPorDia.split(" ")

    somador = 0
    for i in range(len(crimes)):
        somador += int(crimes[i])

    media = float(somador / len(crimes))

    if media <= mediaSecretaria/2:
        continua = False
        break
    
    if media > mediaSecretaria:
        linhasMaiores.append(crimesPorDia)


for linha in linhasMaiores:
    print(linha)####
# user: antonio.oliveira.filho@ccc.ufcg.edu.br
# group: 21.2
# mode: None
# open_datetime: 2022-06-13T17:38:33.743139
# create_datetime: 2022-06-13T17:38:33.743139
# revision: 3
# activity: 5843614150164480
# assignment: 6464005935726592
# ip: 177.37.144.6
# timestamp: 177.37.144.6
