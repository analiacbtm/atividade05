limite = float(input())
soma = 0
b = 0
controle = []
while True:
    numero = input()
    if numero == "fim": break
    numeros = numero.split()
    for a in range(len(numeros)):
        numeros[a] = int(numeros[a])
        soma += numeros[a]
    media = soma/len(numeros)
    soma = 0
    if media <= limite/2:break

    if media > limite:
        controle.append(numero)
for b in range(len(controle)):
    print(controle[b])
####
# user: joao.pedro.porto@ccc.ufcg.edu.br
# group: 21.1e
# mode: None
# open_datetime: 2022-02-27T13:17:32.341491
# create_datetime: 2022-02-27T13:17:32.341491
# revision: 2
# activity: 5219602246139904
# assignment: 5773770079862784
# ip: 2804:14c:da96:81bb:370:25e3:cad7:a480
# timestamp: 2804:14c:da96:81bb:370:25e3:cad7:a480
