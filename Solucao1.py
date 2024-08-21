def soma_valores(lista):
    soma = 0
    for num in lista:
        soma += int(num)
    return soma


limite = float(input())
lista_num = []
while True:
  lista = input().split()
  if lista == ['fim']: break

  media = soma_valores(lista) / len(lista)
  if media <= limite * 0.5: break
  if media > limite:
    lista_num.append(lista)

for i in range(len(lista_num)):
  print(" ".join(lista_num[i]))
####
# user: adriel.carvalho@ccc.ufcg.edu.br
# group: 21.2
# mode: None
# open_datetime: 2022-07-04T13:41:26.968352
# create_datetime: 2022-07-04T13:41:26.968352
# revision: 1
# activity: 5843614150164480
# assignment: 4736767959760896
# ip: 2804:29b8:507a:1c16:7833:9a96:a048:b0d6
# timestamp: 2804:29b8:507a:1c16:7833:9a96:a048:b0d6
