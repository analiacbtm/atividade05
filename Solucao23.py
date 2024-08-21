media_mensal = float(input())
media_diaria = []
while True:
  ocorrencia = input()
  if ocorrencia == "fim":
    for i in media_diaria:
      print(i)
    break
  lista_ocorrencia = ocorrencia.split()
  somador = 0
  for num in range(len(lista_ocorrencia)):
    somador += int(lista_ocorrencia[num])
  media = float(somador / len(lista_ocorrencia))
  if media > media_mensal:
    media_diaria.append(ocorrencia)
  elif media < (media_mensal/2):
    for x in media_diaria:
      print(x)
    break
####
# user: cicero.rocha@ccc.ufcg.edu.br
# group: 21.2
# mode: None
# open_datetime: 2022-08-25T03:35:42.876892
# create_datetime: 2022-08-25T03:35:42.876892
# revision: 1
# activity: 5843614150164480
# assignment: 6545983150227456
# ip: 177.73.206.60
# timestamp: 177.73.206.60
