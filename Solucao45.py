#Prog1 - UFCG - 2/mar/2022
#Aluno: Felipe da Silva Gangorra - 121111084
#ACIMA DA MÉDIA:calculando meses acima da média de ocorrências.

media_geral = float(input())
sequencia = ""

while True:
    dados = input().split()
    
    if  dados[0] == 'fim': break
    
    ocorrencias = 0
    for i in dados:
        ocorrencias += int(i)
    media = (ocorrencias / len(dados)) 
    
    if (media * 2) < media_geral: break
    
    if media > media_geral:
        for i in range(len(dados)):
            if i == (len(dados)-1):
                sequencia += dados[i] + "\n"
            else:
                sequencia += dados[i] + " "

print(sequencia, end = "")####
# user: felipe.gangorra@ccc.ufcg.edu.br
# group: 21.1e
# mode: None
# open_datetime: 2022-03-02T14:51:18.039839
# create_datetime: 2022-03-02T14:51:18.039839
# revision: 1
# activity: 5219602246139904
# assignment: 5876678033145856
# ip: 200.9.26.244
# timestamp: 200.9.26.244
