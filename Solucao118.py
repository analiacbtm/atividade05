media = float(input())

sequencias = []
while True:
    seq = input()
    if seq == "fim":
        break
    soma = 0
    count = 0
    for n in seq.split():
        soma += int(n)
        count += 1
    if soma / count > media:
        sequencias.append(seq)

    if (soma / count) < (media / 2):
        break

for s in sequencias:
    print(s)
####
# user: maria.helena.satyro.gomes.alves@ccc.ufcg.edu.br
# group: 22.1
# mode: None
# open_datetime: 2022-11-09T23:31:54.442246
# create_datetime: 2022-11-09T23:31:54.442246
# revision: 1
# activity: 5843614150164480
# assignment: 5839926530670592
# ip: 2804:29b8:505b:343c:dc41:3adf:d3f8:4058
# timestamp: 2804:29b8:505b:343c:dc41:3adf:d3f8:4058
