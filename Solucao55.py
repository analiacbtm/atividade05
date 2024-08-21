# Prog1 - Gabriel - 119210744
# UFCG - UNIDADE 5 - Acima da media/Criminalidade

limite = float(input())


def menor(soma, seq):
    med = soma / len(seq)
    if med <= limite / 2:
        return True


def maior(soma, seq):
    med = soma / len(seq)
    if med > limite:
        return True


maior_seq = []
while True:
    soma = 0
    seq = input().split()
    if seq[0] == 'fim': break
    for i in seq:
        soma += int(i)
    if menor(soma, seq): break
    elif maior(soma, seq):
        maior_seq.append(seq)

for i in range(len(maior_seq)):
    for j in range(len(maior_seq[i])):
        if j < len(maior_seq[i])-1:
            print(maior_seq[i][j], end=' ')
        elif j == len(maior_seq[i])-1:
            print(maior_seq[i][j])

####
# user: gabriel.soares.ferreira@ccc.ufcg.edu.br
# group: 21.1e
# mode: None
# open_datetime: 2022-02-17T20:15:25.209109
# create_datetime: 2022-02-17T20:15:25.209109
# revision: 1
# activity: 5219602246139904
# assignment: 5907728968974336
# ip: 177.37.144.90
# timestamp: 177.37.144.90
