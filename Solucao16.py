mensal = float(input())
medias = []
contador = 0

def media(sequencia):
   lista = sequencia.split()
   atual = 0
   for k in lista:
       atual += int(k)
   return atual/len(lista)

while True:
   valores = input()

   if valores == "fim" or media(valores) <= mensal/2:
      break

   medias.append(valores)

   if contador >= 2:
      break

for i in medias:
   if media(i) >= mensal:
       print(i)
####
# user: arthur.silva@ccc.ufcg.edu.br
# group: 21.2
# mode: None
# open_datetime: 2022-06-30T04:01:05.088116
# create_datetime: 2022-06-30T04:01:05.088116
# revision: 1
# activity: 5843614150164480
# assignment: 6611030752886784
# ip: 45.228.145.83
# timestamp: 45.228.145.83
