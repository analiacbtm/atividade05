media_ssp = float(input())
saida = []
while True:
    soma = 0
    registro = input()
    registro_separado = registro.split()
    if registro_separado[0] == 'fim': break
    for i in range(len(registro_separado)):
        soma += int(registro_separado[i])
    media = soma / len(registro_separado)
    if media > media_ssp:
        saida.append(registro)
    if media * 2 < media_ssp: break
for j in range(len(saida)):
    print(saida[j])
####
# user: hildon.regis.navarro.neto@ccc.ufcg.edu.br
# group: 22.1
# mode: lista5
# open_datetime: 2022-12-19T20:28:48.466287
# create_datetime: 2022-12-19T20:28:48.466287
# revision: 1
# activity: 5843614150164480
# assignment: 5524451451994112
# ip: 177.37.144.82
# timestamp: 177.37.144.82
