media_base = float(input())

ocorrencias = list()
while True:
    registro = input()
    if registro == 'fim': break
    
    registro = [int(n) for n in registro.split()]
    media = sum(registro) / len(registro)

    if media < media_base / 2: break
    ocorrencias.append(registro)

for valores in ocorrencias:
    if sum(valores) / len(valores) > media_base:
        saida = ''
        for v in valores:
            saida += str(v) 
            saida += ' '
        print(saida[:-1])####
# user: jackson.souza@ccc.ufcg.edu.br
# group: 21.1e
# mode: None
# open_datetime: 2022-02-16T14:23:28.201991
# create_datetime: 2022-02-16T14:23:28.201991
# revision: 1
# activity: 5219602246139904
# assignment: 4952512874414080
# ip: 45.4.145.241
# timestamp: 45.4.145.241
