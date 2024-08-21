media = float(input())

while True:
    saida = ''
    entrada = input()
    if entrada == 'fim': break
    entrada = [int(n) for n in entrada.split()]
    dividendo = 0
    divisor = len(entrada)
    i = 0
    while i < divisor:
        dividendo += entrada[i]
        i += 1
    media_entrada = dividendo/divisor
    if media_entrada <= media/2:
        break
    if media_entrada > media:
        ind = 0
        while ind < len(entrada):
            if ind == len(entrada) - 1:
                saida += str(entrada[ind])
                ind += 1
            else:
                saida += f'{str(entrada[ind])} '
                ind += 1
        print(saida)
####
# user: geraldo.lima.junior@ccc.ufcg.edu.br
# group: 22.1
# mode: None
# open_datetime: 2022-11-13T22:00:46.630967
# create_datetime: 2022-11-13T22:00:46.630967
# revision: 1
# activity: 5843614150164480
# assignment: 5910752823083008
# ip: 150.165.42.185
# timestamp: 150.165.42.185
