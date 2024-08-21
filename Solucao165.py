maioreslist = []
media = float(input())

while True:
    seq = input()
    if seq == 'fim': break
    numbers = seq.split()

    count = 0
    soma = 0

    while True:
        if count == len(numbers): break
        soma += int(numbers[count])
        media2 = soma / len(numbers)
        if media2 > media and count == len(numbers) - 1:
            maioreslist.append(seq)

        count += 1

    if media2 <= (media / 2): break

count = 0

while True:
    if count == len(maioreslist): break
    print(maioreslist[count])

    count += 1


####
# user: yalle.silva@ccc.ufcg.edu.br
# group: 21.1e
# mode: None
# open_datetime: 2022-02-16T21:49:35.317605
# create_datetime: 2022-02-16T21:49:35.317605
# revision: 2
# activity: 5219602246139904
# assignment: 6128283693350912
# ip: 186.233.254.177
# timestamp: 186.233.254.177
