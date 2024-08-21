estab = float(input())

while True:
    saida = ''
    dia = input().split()
    if dia == ['fim']: break
    soma = 0
    cont = 0

    for c in dia:
        soma += int(c)
        cont +=1
    media = soma // cont

    if media < estab / 2:
        break

    if media > estab:
        i = 0
        while i < len(dia):
            if i == len(dia) - 1:
                saida += f'{dia[i]}'
            else:
                saida += f'{dia[i]} '
            i += 1

        print(saida)

    

















####
# user: joao.pedro.martins.rodrigues@ccc.ufcg.edu.br
# group: 22.1
# mode: lista5
# open_datetime: 2022-12-19T19:05:35.155630
# create_datetime: 2022-12-19T19:05:35.155630
# revision: 1
# activity: 5843614150164480
# assignment: 5538975940870144
# ip: 177.73.204.16
# timestamp: 177.73.204.16
