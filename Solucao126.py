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
# user: noel.aklou@ccc.ufcg.edu.br
# group: 21.2
# mode: None
# open_datetime: 2022-06-20T01:34:47.498032
# create_datetime: 2022-06-20T01:34:47.498032
# revision: 1
# activity: 5843614150164480
# assignment: 5961761989591040
# ip: 177.37.145.68
# timestamp: 177.37.145.68
