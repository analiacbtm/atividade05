media_mensal = float(input())
lista_valores_validos = []
media = 0 

while True:
  valores_dia = input()

  if valores_dia == 'fim':
    break

  lista = list(valores_dia.split(' '))
  soma = 0
  
  for num in lista:
    soma += int(num)

  media = soma / len(lista)

  if media > media_mensal:
    lista_valores_validos.append(valores_dia)

  
  if media < media_mensal / 2 :
    break
  

for x in lista_valores_validos:
  print(x)
####
# user: larysa.almeida@ccc.ufcg.edu.br
# group: 21.2
# mode: None
# open_datetime: 2022-06-17T18:01:11.204353
# create_datetime: 2022-06-17T18:01:11.204353
# revision: 1
# activity: 5843614150164480
# assignment: 5314006430515200
# ip: 177.37.144.38
# timestamp: 177.37.144.38
