ssp = float(input())
while True:
    registros = input()
    if registros == "fim":
        break
    else:
        seq = ""
        soma = 0
        quantidadedenumero = 0
        reg = registros.split()
        for e in reg:
            inteiro = int(e)
            quantidadedenumero += 1
            soma += inteiro

        if soma/quantidadedenumero < ssp/2:
            break
            
        elif soma/quantidadedenumero > ssp:
            seq += registros
            print(seq)
####
# user: maria.clara.oliveira.guedes@ccc.ufcg.edu.br
# group: 22.1
# mode: lista5
# open_datetime: 2022-12-20T16:46:14.153761
# create_datetime: 2022-12-20T16:46:14.153761
# revision: 1
# activity: 5843614150164480
# assignment: 5229006204960768
# ip: 177.37.147.19
# timestamp: 177.37.147.19
