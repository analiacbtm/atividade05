#UFCG
#Welly Remígio Bezerra
#Calcula a média de uma sequência e retorna a mesma caso esta tiver média maior que a média informada pelo usuário.

def calcula_Media(valores):
    tamanho = len(valores)
    somaMedia = 0
    for i in range(tamanho):
        somaMedia += int(valores[i])
        media = somaMedia/tamanho
    return media


sequencia = []
mediaSSP = float(input())
while True:
    valores = input()
    lista = valores.split()
    if(lista == ["fim"]):
        break

    else:
        media = calcula_Media(lista)
        if(media > mediaSSP):
            sequencia.append(valores)
        if(media < mediaSSP/2):
            break

for i in sequencia:
    print(i)



####
# user: welly.bezerra@ccc.ufcg.edu.br
# group: 21.2
# mode: None
# open_datetime: 2022-06-30T00:51:07.481404
# create_datetime: 2022-06-30T00:51:07.481404
# revision: 4
# activity: 5843614150164480
# assignment: 5725263004434432
# ip: 2804:29b8:505a:3ed5:a53c:f1c4:4915:1d96
# timestamp: 2804:29b8:505a:3ed5:a53c:f1c4:4915:1d96
