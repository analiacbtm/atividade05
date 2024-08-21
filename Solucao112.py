ocorrencias          = []
valores_individuais  = []
inventario_de_linhas = []
controle_if          = True
controle_break       = False

media = float(input())
while True:
    i = 0
    entrada = input()
    if entrada == "fim": break
    ocorrencias.append(entrada)
    valores_individuais = entrada.split(" ")
    
    for i in range(len(valores_individuais)):
        valores_individuais[i] = int(valores_individuais[i])
        if valores_individuais[i] > media and controle_if == True:
            inventario_de_linhas.append(entrada)
            controle_if = False
        if valores_individuais[i] < (media/2):
            controle_break = True
    if controle_break == True: break

    controle_if = True
    controle_break = False

i = 0
for i in range(len(inventario_de_linhas)):
    print(inventario_de_linhas[i])
####
# user: luiz.sergio.alves.filho@ccc.ufcg.edu.br
# group: 21.1e
# mode: None
# open_datetime: 2022-02-18T20:44:10.393466
# create_datetime: 2022-02-18T20:44:10.393466
# revision: 1
# activity: 5219602246139904
# assignment: 5875828602699776
# ip: 177.37.147.105
# timestamp: 177.37.147.105
