import string
import sys

media_mensal = float(input())
media_limite = media_mensal / 2

nums, num = [], ''
while True:
    valores = input()
    if valores == 'fim': break
    sequencia = valores.split()

    soma, media = 0, 0
    for i in sequencia:
        soma += int(i)

    media = soma / len(sequencia)

    if media < media_limite: break
    if media > media_mensal:
        nums.append(valores)
        num = '\n'.join(nums)

if len(num) == 0:
    sys.exit()

print(num)
####
# user: thayane.stheffany.barros@ccc.ufcg.edu.br
# group: 21.1e
# mode: None
# open_datetime: 2022-02-15T19:24:10.949085
# create_datetime: 2022-02-15T19:24:10.949085
# revision: 1
# activity: 5219602246139904
# assignment: 5889743457878016
# ip: 2804:29b8:5077:195:8099:ddc5:ba1c:f277
# timestamp: 2804:29b8:5077:195:8099:ddc5:ba1c:f277
