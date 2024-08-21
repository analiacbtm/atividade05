# coding: utf-8
# Universidade Federal de Campina Grande - UFCG
# Programação 1 | Fev,2022
# Mayara Brito - 121110615
# Ocorrencias acima da média

media_ssp = float(input())
sequencia = ""

while True:
    dados = input().split()
    
    if  dados[0] == 'fim': break
    
    oc = 0
    for e in dados:
        oc += int(e)
    media = (oc / len(dados)) 
    
    if (media * 2) < media_ssp: break
    
    if media > media_ssp:
        for i in range(len(dados)):
            if i == (len(dados)-1):
                sequencia += dados[i] + "\n"
            else:
                sequencia += dados[i] + " "

print(sequencia, end = "")
####
# user: mayara.pinheiro@ccc.ufcg.edu.br
# group: 21.1e
# mode: None
# open_datetime: 2022-02-16T14:42:55.830369
# create_datetime: 2022-02-16T14:42:55.830369
# revision: 5
# activity: 5219602246139904
# assignment: 5212645722423296
# ip: 187.95.226.10
# timestamp: 187.95.226.10
