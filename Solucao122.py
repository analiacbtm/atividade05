# Entrada da media mensal estabelecida pela ssp:
N = float(input())

# Entrada das sequencias de qtd de ocorrencias registradas:
lista_media_mensal_maior_q_limite = []
while True:
    sequencia = input().split()
    if sequencia[0] == "fim": break
    soma = 0
    for i in range(len(sequencia)):
        soma += int(sequencia[i])
    if soma / len(sequencia) < 0.5 * N: break
    if soma / len(sequencia) > N:
        lista_media_mensal_maior_q_limite.append(sequencia)

# Cada sequencia em lista_media_maior_q_limite está sendo lida como uma lista. Precisamos converter essas listas em strings.

lista = lista_media_mensal_maior_q_limite

for sequencia in lista:
    sequenciaa = ""
    for i in range(len(sequencia)):
        if i == len(sequencia) - 1:
            sequenciaa += sequencia[i]
        else:
            sequenciaa += sequencia[i] + " "
    print(sequenciaa)
####
# user: miguel.ferreira@ccc.ufcg.edu.br
# group: 21.1e
# mode: None
# open_datetime: 2022-02-14T23:29:36.897787
# create_datetime: 2022-02-14T23:29:36.897787
# revision: 1
# activity: 5219602246139904
# assignment: 5102292242006016
# ip: 191.35.82.126
# timestamp: 191.35.82.126
