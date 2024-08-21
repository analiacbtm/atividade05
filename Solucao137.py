media_alvo = float(input())
lista_medias_altas = []

while True:
    sequencia = input()
    if sequencia == 'fim':
        break  
    
    lista_mes = sequencia.split()
    soma = 0
    for mes in lista_mes:
        soma += int(mes)
    media = soma/len(lista_mes)
    
    if media > media_alvo:
        lista_medias_altas.append(sequencia)    
    if media*2 < media_alvo:
        break
for n in lista_medias_altas:
    print (n)

####
# user: rafael.luis.carvalho.maia@ccc.ufcg.edu.br
# group: 22.1
# mode: None
# open_datetime: 2022-11-09T01:53:05.917745
# create_datetime: 2022-11-09T01:53:05.917745
# revision: 1
# activity: 5843614150164480
# assignment: 6431159649042432
# ip: 2804:29b8:505b:d8fc:3d3d:7277:c535:f3a5
# timestamp: 2804:29b8:505b:d8fc:3d3d:7277:c535:f3a5
