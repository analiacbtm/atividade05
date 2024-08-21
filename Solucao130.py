media_ssp = float(input())

saidas = []

if media_ssp == 0:
    quit()

while True:
    valores, processos, media = [], [], 0

    val = input()
    valores = val.split()
    
    if val.lower() == 'fim':
        break

    for valor in range(len(valores)):
        processos.append(int(valores[valor]))
        media += processos[valor] 
    
    media = media / len(processos)

    if media < (media_ssp / 2): break
        
    if media > media_ssp:
        saidas.append(val)
    
for saida in saidas:
    print(saida)
####
# user: paulo.ricardo.pereira.nascimento@ccc.ufcg.edu.br
# group: 22.1
# mode: None
# open_datetime: 2022-11-09T23:36:43.344407
# create_datetime: 2022-11-09T23:36:43.344407
# revision: 5
# activity: 5843614150164480
# assignment: 4925591746772992
# ip: 177.84.217.116
# timestamp: 177.84.217.116
