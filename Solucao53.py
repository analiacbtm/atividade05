def media_criminalidade(entrada, sequencia):
    valores = sequencia.split(" ")
    soma = 0
    for valor in valores:
        soma += float(valor)
    media = soma / len(valores)
    if media > entrada:
        return True
    else:
        return False
    
sequencias = []
entrada = float(input())

while True:
    sequencia = input()
    if sequencia == 'fim':
        break
    sequencias.append(sequencia)
for linha in sequencias:
    if media_criminalidade(entrada, linha):
        print(linha)
####
# user: gabriel.emannuel.gama.andrade@ccc.ufcg.edu.br
# group: 22.1
# mode: None
# open_datetime: 2022-11-21T13:06:34.087342
# create_datetime: 2022-11-21T13:06:34.087342
# revision: 2
# activity: 5843614150164480
# assignment: 4741552112926720
# ip: 187.183.197.234
# timestamp: 187.183.197.234
