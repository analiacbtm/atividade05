media = float(input())
res = []

while True:
 valores = input()
 if valores == 'fim':
  break
 else:
  soma = 0
  novaMedia = 0
  valoresLista = valores.split()
  for i in range(len( valoresLista)):
   soma += int(valoresLista[i])
  novaMedia = soma/len(valoresLista)
 
  if novaMedia * 2 < media:
   break
  if novaMedia > media:
   res.append(valores)

for i in range(len(res)):
 print(res[i])
####
# user: daniele.oliveira.sousa@ccc.ufcg.edu.br
# group: 22.1
# mode: None
# open_datetime: 2022-11-10T00:05:12.707178
# create_datetime: 2022-11-10T00:05:12.707178
# revision: 1
# activity: 5843614150164480
# assignment: 5838376248803328
# ip: 177.37.145.244
# timestamp: 177.37.145.244
