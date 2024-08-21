official_avarage = float(input())
months = []

while True:
    day_avarage = 0
    day_register = []
    data_input = input()
    data_splitted = data_input.split(" ")

    if data_input == "fim": break

    day_register = [int(x) for x in data_splitted]


    for n in day_register:
        day_avarage +=n

    day_avarage = day_avarage/ len(day_register)

    if day_avarage <= official_avarage/2:break

    if day_avarage > official_avarage:
        months.append(data_input)

for item in months:
    print(item)
####
# user: pedro.henrique.veloso.fernandes@ccc.ufcg.edu.br
# group: 22.1
# mode: None
# open_datetime: 2022-11-14T19:39:27.071233
# create_datetime: 2022-11-14T19:39:27.071233
# revision: 1
# activity: 5843614150164480
# assignment: 6240369752670208
# ip: 2804:7f7:2483:d9f3:894e:77ce:444e:9684
# timestamp: 2804:7f7:2483:d9f3:894e:77ce:444e:9684
