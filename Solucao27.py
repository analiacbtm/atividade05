media_ssp = float(input())

saida = []

while True:
  entrada = input()

  soma_linha = 0
  media_linha = 0

  if entrada == 'fim': break

  valor = entrada.split()

  for v in range(len(valor)):
    soma_linha += int(valor[v])

  media_linha = soma_linha / len(valor)

  if media_linha < (media_ssp) / 2: break

  if media_linha > media_ssp:
     saida.append(valor)
   

for elemento in saida:
  formatada = ""
  for v in range(len(elemento) - 1):
    formatada += f'{elemento[v]} '
  
  formatada += f'{elemento[-1]}'
  print(formatada)
####
# user: danielly.rayanne.macedo.lima@ccc.ufcg.edu.br
# group: 22.1
# mode: None
# open_datetime: 2022-11-07T14:16:00.410975
# create_datetime: 2022-11-07T14:16:00.410975
# revision: 2
# activity: 5843614150164480
# assignment: 4991271628177408
# ip: 2804:29b8:505a:24ae:983e:3f58:81f8:ac2a
# timestamp: 2804:29b8:505a:24ae:983e:3f58:81f8:ac2a
