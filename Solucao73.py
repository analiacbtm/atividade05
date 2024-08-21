def calcula_media(dados):
   soma = 0
   ocorrencias = dados.split()
   for i in range(len(ocorrencias)):
      soma += int(ocorrencias[i])
   media = soma/len(ocorrencias)
   return media

media_mensal = float(input())
lista = []


while True:
   dados = input()
   if dados == "fim":
      break

   lista.append(dados)
   if calcula_media(dados) < (media_mensal/2):
      break


i = 0
while i < len(lista):
   if calcula_media(lista[i]) > media_mensal:
      print(lista[i])
   i+=1
####
# user: isabelle.silva.antunes@ccc.ufcg.edu.br
# group: 22.1
# mode: lista5
# open_datetime: 2022-12-20T19:06:00.799159
# create_datetime: 2022-12-20T19:06:00.799159
# revision: 1
# activity: 5843614150164480
# assignment: 5076507284209664
# ip: 177.37.144.192
# timestamp: 177.37.144.192
