media = input()
maiores = []
while True:
    entrada = input().split()
    soma = 0

    if entrada[0]  == "fim":
        break

    for i in range(len(entrada)):
        soma += int(entrada[i])

    soma = soma/len(entrada)

    if soma > float(media):
        maiores.append(entrada)
    elif float(media)/2 >= soma:
        break

for j in range(len(maiores)):
    interador = iter(maiores[j])
    for l in range(len(maiores[j])):
        if l == len(maiores[j]) - 1:
            print(next(interador))
            break
        print(next(interador), end=" ")
####
# user: erik.luan.rodrigues.florencio@ccc.ufcg.edu.br
# group: 22.1
# mode: None
# open_datetime: 2022-11-10T19:48:30.953750
# create_datetime: 2022-11-10T19:48:30.953750
# revision: 4
# activity: 5843614150164480
# assignment: 5557737381429248
# ip: 168.228.210.249
# timestamp: 168.228.210.249
