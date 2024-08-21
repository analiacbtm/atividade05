media_mensal = float(input())
media_limite = media_mensal/2


seqs_acima = []

while True:
    seq_input = input()
    if seq_input == 'fim':
        break

    lst_seq = seq_input.split()

    soma = 0
    media_seq = 0

    for num in lst_seq:
        soma += int(num)

    media_seq = soma / len(lst_seq)
    if media_seq <= media_limite:
        break
    if media_seq > media_mensal:
        seqs_acima.append(lst_seq)


for lst in seqs_acima:
    print(' '.join(lst))
####
# user: fernando.torres@ccc.ufcg.edu.br
# group: 21.1e
# mode: None
# open_datetime: 2022-02-14T11:16:11.219463
# create_datetime: 2022-02-14T11:16:11.219463
# revision: 2
# activity: 5219602246139904
# assignment: 5785217275002880
# ip: 168.0.233.3
# timestamp: 168.0.233.3
