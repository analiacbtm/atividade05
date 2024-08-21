def somar_elementos(valores):
  soma = 0
  for numero in valores:
    soma += numero
  return soma
def converter(teste_2):
  valores = []
  for val in teste_2:
   valores.append(int(val))
  return valores
  
entrada_1 = float(input())
valores=[]
teste=0
teste_2 = ''
dias = ''
while True:
  entrada_2 = input()
  teste_2 = entrada_2
  if entrada_2 == 'fim' :
    break
  else:
    teste_2 = entrada_2.split()
    valores = converter(teste_2)
    teste = somar_elementos(valores)
    if teste/ len(valores) > entrada_1:
     dias = entrada_2
     print(dias)
    elif teste/len(valores)< entrada_1 /2 :
      break
      
####
# user: joaquim.souza@ccc.ufcg.edu.br
# group: 21.2
# mode: None
# open_datetime: 2022-07-28T21:35:55.301023
# create_datetime: 2022-07-28T21:35:55.301023
# revision: 2
# activity: 5843614150164480
# assignment: 5248097774993408
# ip: 177.37.146.73
# timestamp: 177.37.146.73
