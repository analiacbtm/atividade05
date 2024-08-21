media=float(input())

lista=[]
while True:
  soma=0
  count=0
  sequencia=input()
  if sequencia=='fim':
    break
  aux=sequencia.split()
  for i in aux:
    soma+=int(i)
    count+=1
  if 2*(soma/count)<media:
    break
  if (soma/count)> media:
    lista.append(sequencia)
                                                                  
for i in range(len(lista)):
  print(lista[i])
####
# user: nubia.siqueira@ccc.ufcg.edu.br
# group: 21.1e
# mode: None
# open_datetime: 2022-02-16T14:09:19.347334
# create_datetime: 2022-02-16T14:09:19.347334
# revision: 1
# activity: 5219602246139904
# assignment: 6426216984739840
# ip: 177.37.146.55
# timestamp: 177.37.146.55
