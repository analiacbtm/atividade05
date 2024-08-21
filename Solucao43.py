media = float(input())
saida = []

while True:
	regs = input()
	if regs == "fim":
		break
	dados = regs.split()
	soma = 0
	for i in dados:
		soma += int(i)
		medi = soma/len(dados)
	if medi * 2<media:
		break
	if medi>media:
		saida.append(regs)
		
for j in saida:
	print(j)
####
# user: ewerthon.tavares@ccc.ufcg.edu.br
# group: 22.1
# mode: None
# open_datetime: 2022-11-28T14:28:02.551051
# create_datetime: 2022-11-28T14:28:02.551051
# revision: 1
# activity: 5843614150164480
# assignment: 6258816100335616
# ip: 2804:7f7:2480:9dc2:dc15:c1b:c688:a3f5
# timestamp: 2804:7f7:2480:9dc2:dc15:c1b:c688:a3f5
