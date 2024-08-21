ssp_m = float(input())
lista = ''
mystr = 'abcdes'

while True:
    seq = input().split()
    if seq[0] == 'fim': break
    media = 0
    for valor in seq:
        media += int(valor)/len(seq)
    if media > ssp_m:
        for valor2 in seq:
            lista += (f'{valor2} ')
        lista = lista.strip()
        lista += '\n'
    if media < ssp_m/2: break

if lista:
    print(lista.strip())
####
# user: marcos.dirley.lima.silva@ccc.ufcg.edu.br
# group: 22.1
# mode: None
# open_datetime: 2022-11-12T20:11:47.401649
# create_datetime: 2022-11-12T20:11:47.401649
# revision: 2
# activity: 5843614150164480
# assignment: 4861002887725056
# ip: 2804:29b8:505e:ba9:79a3:aa97:127d:3097
# timestamp: 2804:29b8:505e:ba9:79a3:aa97:127d:3097
