media = float(input())
resposta = []
while True:
    soma = 0
    valores = input()
    if valores == "fim": break
    else:
        individuais = valores.split()
        for n in individuais:
            soma += float(n)
        if soma // len(individuais) < media / 2: break
        if soma // len(individuais) > media:
            resposta.append(valores)

for r in resposta:
    print(r)
####
# user: andre.figueiredo.castro.cunha@ccc.ufcg.edu.br
# group: 22.1
# mode: lista5
# open_datetime: 2022-12-17T18:26:06.004109
# create_datetime: 2022-12-17T18:26:06.004109
# revision: 2
# activity: 5843614150164480
# assignment: 6059568926818304
# ip: 181.223.163.169
# timestamp: 181.223.163.169
