def sum(array):
    total = 0
    for i in range(0, len(array)):
        total += int(array[i])
    return total

averages = []
expectedAverage = float(input())

while True:
  monthAverages = input()
  averageValues = monthAverages.split(' ')
  if (monthAverages == 'fim'):
    break
  if (sum(averageValues) / len(averageValues) < expectedAverage / 2):
    break
  if (sum(averageValues) / len(averageValues) > expectedAverage):
    averages += [monthAverages]

for average in averages:
  print(average)####
# user: dhouglas.nobrega@ccc.ufcg.edu.br
# group: 21.2
# mode: None
# open_datetime: 2022-06-20T13:23:03.982845
# create_datetime: 2022-06-20T13:23:03.982845
# revision: 3
# activity: 5843614150164480
# assignment: 5316371900530688
# ip: 34.134.142.56
# timestamp: 34.134.142.56
