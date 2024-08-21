media = float(input())

while True:
	entrada = input()
	if entrada == 'fim':
		break
	soma = 0
	nums = entrada.split()
	for n in nums:
		soma += int(n)
	m = soma / len(nums)
	if m * 2 < media:
		break
	if m > media:
		print(entrada)
####
# user: mateus.medeiros.faria@ccc.ufcg.edu.br
# group: 22.1
# mode: None
# open_datetime: 2022-11-07T21:07:27.122292
# create_datetime: 2022-11-07T21:07:27.122292
# revision: 1
# activity: 5843614150164480
# assignment: 5319972488216576
# ip: 181.223.167.236
# timestamp: 181.223.167.236
