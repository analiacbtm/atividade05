media = float(input())

while True:
   linha = input()
   if linha == 'fim': break
   soma = 0
   dias = linha.split(' ')
   
   for i in dias:
      soma += int(i)
   m = soma / len(dias)

   if m * 2 < media:
      break
   
   if m > media:
      print(linha)
####
# user: eliane.tamara.lima.oliveira@ccc.ufcg.edu.br
# group: 22.1
# mode: None
# open_datetime: 2022-11-09T13:31:23.966515
# create_datetime: 2022-11-09T13:31:23.966515
# revision: 2
# activity: 5843614150164480
# assignment: 6505530497433600
# ip: 177.70.177.143
# timestamp: 177.70.177.143
