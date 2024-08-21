ssp = float(input())
maior = []

while True:
    sequencia = input()
    
    if sequencia == 'fim': break
    
    lsequencia = sequencia.split()
    
    soma = 0
    
    for i in lsequencia:
        soma += int(i)
    
    media = soma / len(lsequencia)
    
    if media < ssp / 2: break
    
    if media > ssp:
        maior.append(sequencia)

for a in maior:
    print(a)
####
# user: lucas.leones.santos@ccc.ufcg.edu.br
# group: 21.1e
# mode: None
# open_datetime: 2022-02-16T17:22:16.399181
# create_datetime: 2022-02-16T17:22:16.399181
# revision: 1
# activity: 5219602246139904
# assignment: 5283858763218944
# ip: 177.75.23.104
# timestamp: 177.75.23.104
