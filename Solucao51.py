mensal = float(input())
maioreslimite = []

while True:
    sequencia = input()
    if sequencia == 'fim': break
    valores = sequencia.split()
    soma = 0
    for c in valores:
        soma += int(c)
    media = soma / len(valores)
    if media > mensal: maioreslimite.append(sequencia)
    if media < mensal/2: break

for c in maioreslimite:
    print(c)
####
# user: gabriel.dantas.oliveira@ccc.ufcg.edu.br
# group: 21.1e
# mode: None
# open_datetime: 2022-02-23T13:31:35.602557
# create_datetime: 2022-02-23T13:31:35.602557
# revision: 1
# activity: 5219602246139904
# assignment: 5854280885993472
# ip: 45.226.140.15
# timestamp: 45.226.140.15
