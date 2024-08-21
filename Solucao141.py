monthly_average = float(input())
crimes_per_month = []

while True:
    new_data = input()
    if new_data == "fim": break
    number_sequence = [int(x) for x in new_data.split()]
    crimes_per_month.append(number_sequence)

for monthly_data in crimes_per_month:
    current_sum = 0
    to_print = ""
    for i in range(len(monthly_data)):
        current_sum += int(monthly_data[i])
        if i == len(monthly_data) - 1:
            to_print += f"{monthly_data[i]}"
        else:
            to_print += f"{monthly_data[i]} "
    month_average = current_sum / len(monthly_data)
    if month_average > monthly_average: print(to_print)   ####
# user: rodrigo.rodrigues@ccc.ufcg.edu.br
# group: 21.1e
# mode: None
# open_datetime: 2022-02-16T13:03:51.737850
# create_datetime: 2022-02-16T13:03:51.737850
# revision: 1
# activity: 5219602246139904
# assignment: 5775595675844608
# ip: 177.72.190.91
# timestamp: 177.72.190.91
