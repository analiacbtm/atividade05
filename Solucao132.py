media_ssp = float(input())
saida = []
while True:
    entradas = input().split()
    
    if entradas[0] == "fim": break
    entradas = [int(x) for x in entradas]
    
    if (sum(entradas) / len(entradas)) > media_ssp: 
        saida.append(entradas)

    if (sum(entradas) / len(entradas)) < (media_ssp / 2): break

for x in saida:
    resp = ''
    for j in range(len(x)):
        if j!= len(x)-1:
            resp += str(x[j]) + ' '
        if j == len(x)-1:
            resp += str(x[j])
    print(resp)####
# user: pedro.henrique.costa@ccc.ufcg.edu.br
# group: 21.2
# mode: None
# open_datetime: 2022-06-13T15:51:41.126651
# create_datetime: 2022-06-13T15:51:41.126651
# revision: 2
# activity: 5843614150164480
# assignment: 5880817643421696
# ip: 177.37.147.141
# timestamp: 177.37.147.141
