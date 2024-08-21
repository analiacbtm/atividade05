def converter(valores):
  for valor in range(len(valores)):
    valores[valor] = int(valores[valor])
  return valores


def calcula_media(valores_inteiros):
  s = 0
  c = 0
  for valor in valores_inteiros:
    s += valor
    c += 1
  media = s / c
  return media


def main():
  media_mensal = float(input())
  resposta = []
  while True:
    valores = input()
    valores_list = valores.split()
    if valores_list[0] == 'fim': break
    valores_inteiros = converter(valores_list)
    media = calcula_media(valores_inteiros)
    if media > media_mensal:
      resposta.append(valores)
    if media_mensal / media > 2: break
    else:
      media = 0
  for item in resposta:
    print(item)



main()

####
# user: joao.pedro.angelo@ccc.ufcg.edu.br
# group: 21.2
# mode: None
# open_datetime: 2022-06-19T15:21:08.842668
# create_datetime: 2022-06-19T15:21:08.842668
# revision: 2
# activity: 5843614150164480
# assignment: 6594664947777536
# ip: 2804:29b8:505a:9244:d425:853e:a82a:e951
# timestamp: 2804:29b8:505a:9244:d425:853e:a82a:e951
