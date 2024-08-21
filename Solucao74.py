def media_sequencia(seq):
  soma = 0
  for v in seq:
    soma = soma + v
  media = soma / len(seq)
  return media

limit = float(input())

linhas = []

while True:
  linha = input()
  if linha == 'fim':
    break
  
  tokens = linha.split(' ')
  
  sequencia = [int(v) for v in tokens]

  media = media_sequencia(sequencia)

  if media < (limit / 2):
    break

  if media >= limit:
    linhas.append(linha)

for linha in linhas:
  print(linha)
####
# user: israel.buriti.galvao@ccc.ufcg.edu.br
# group: 22.1
# mode: None
# open_datetime: 2022-11-08T17:50:04.599080
# create_datetime: 2022-11-08T17:50:04.599080
# revision: 1
# activity: 5843614150164480
# assignment: 5277650551570432
# ip: 2804:29b8:507a:c24:2fe:5863:5d03:18e9
# timestamp: 2804:29b8:507a:c24:2fe:5863:5d03:18e9
