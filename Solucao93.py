ssp = float(input())
lista = []
maior = ''
ponto = False
while True:
    entrada = input()
    if entrada == 'fim':
        break
    else:
       for n in entrada.split():
          if int(n) > ssp:
             lista.append(entrada)
             break
       soma = 0
       media = 0
       i = 0
       for num in entrada.split():
             soma += int(num)
             i += 1
       media = soma / i
    if media < ssp / 2:
       break


for seq in lista:
    print(seq)

####
# user: laura.menezes.batista@ccc.ufcg.edu.br
# group: 22.1
# mode: None
# open_datetime: 2022-11-08T20:09:49.892127
# create_datetime: 2022-11-08T20:09:49.892127
# revision: 2
# activity: 5843614150164480
# assignment: 4953416021311488
# ip: 2804:29b8:505d:59bb:ae3f:68e6:3c82:625d
# timestamp: 2804:29b8:505d:59bb:ae3f:68e6:3c82:625d
