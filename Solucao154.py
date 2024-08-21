def media_aritmetica(seq):
    qtd = len(seq)
    soma = 0
    for e in seq:
        soma += e
    return soma/qtd

def my_print(seq):
    for i in range(len(seq)-1):
        print(seq[i], end=" ")
    print(seq[-1])

media = media_ssp = float(input())
entrada = input()
saida = []
while entrada != "fim":
    seq = [int(num) for num in entrada.split()]
    media = media_aritmetica(seq)
    if media > media_ssp:
        saida.append(seq)
    elif media*2 < media_ssp:
        break
    entrada = input()

for s in saida:
    my_print(s)
####
# user: victor.emanuel.barbosa.rodrigues@ccc.ufcg.edu.br
# group: 22.1
# mode: None
# open_datetime: 2022-11-10T17:28:53.064945
# create_datetime: 2022-11-10T17:28:53.064945
# revision: 1
# activity: 5843614150164480
# assignment: 5001237126709248
# ip: 2804:29b8:5059:c88d:36f4:df31:7c9:dfaf
# timestamp: 2804:29b8:5059:c88d:36f4:df31:7c9:dfaf
