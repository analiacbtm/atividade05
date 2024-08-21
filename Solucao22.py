#Universidade Federal de Campina Grande (UFCG) - CEEI
#Disciplina de Programação 01 e Laboratório de Programação 01 (2021.1) - Turma 01
#Aluna: Catarina Ramalho dos Santos | Matrícula: 121110708
#Questão: Acima da Média (Unidade 5)

mediassp = float(input())
valores = []
while True:
  entrada = input().split()
  if entrada[0] == "fim":
    break
  soma = 0
  sequencia = ""
  for i in range(len(entrada)):
    soma += int(entrada[i])
  media = soma / len(entrada)
  if (media * 2) < mediassp:
    break
  if media > mediassp:
    for c in range(len(entrada)):
      if c == len(entrada) - 1:
        sequencia += entrada[c]
      else:
        sequencia += entrada[c] + " "
    valores.append(sequencia)

for b in valores:
  print(b)
####
# user: catarina.santos@ccc.ufcg.edu.br
# group: 21.1e
# mode: None
# open_datetime: 2022-02-10T03:05:22.796531
# create_datetime: 2022-02-10T03:05:22.796531
# revision: 1
# activity: 5219602246139904
# assignment: 4962369119715328
# ip: 2804:29b8:5077:634:3e2d:2f0d:9ce7:cce7
# timestamp: 2804:29b8:5077:634:3e2d:2f0d:9ce7:cce7
