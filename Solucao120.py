def f_sum(lista):
    soma = 0
    for i in lista:
        soma += int(i)
    return soma

def fim(lista):
    for i in lista:
        if i == "fim":
            return True
    return False

ssp = float(input())
laux = []

while True:
    lista = [x for x in input().split()]
   
    if fim(lista):
        break
    else:
        media = f_sum(lista)/len(lista)

        if  media*2<ssp:
            break;
        elif media > ssp:
            laux+=lista
            laux.append("!")
            lista = []

for i in range(len(laux)):
    if laux[i] == "!":
        print("")
    elif laux[i+1] != "!":
        print(laux[i],end=" ")
    else:
        print(laux[i],end="")

####
# user: matheus.medeiros.germano@ccc.ufcg.edu.br
# group: 22.1
# mode: None
# open_datetime: 2022-11-07T14:08:57.857438
# create_datetime: 2022-11-07T14:08:57.857438
# revision: 2
# activity: 5843614150164480
# assignment: 5186718376394752
# ip: 2804:29b8:505a:4c8a:105c:e9d7:be5d:67bf
# timestamp: 2804:29b8:505a:4c8a:105c:e9d7:be5d:67bf
