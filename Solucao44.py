# O programa lê uma média que será utilizada como critério de Comparação
# O programa recebe uma sequência, e verifica se é uma sentinela...
	# SENTINELA 1: 'fim'
	# SENTINELA 2: receber uma sequência cuja média seja 2 vezes menor que o limite
# Eu tenho que ler a primeira sequência, já calcular a média e guardar
# Leio sequências e guardo médias ENQUANTO não digitar as sentinelas
# No fim, comparo entre os valores guardados a maior média e á associo com uma string

# Leitura dos dados
ssp = float(input())
lista_medias = []
sequencia_strings = []
cont = 0
while True:
	soma = 0
	string = ''
	sequencia = input()
	cont += 1
	if sequencia == "fim": break
	valores = sequencia.split()
	for x in range(len(valores)):
		if x < len(valores) - 1:
			string += valores[x] + ' '
		if x == len(valores) - 1:
			string += valores[x]
		n = int(valores[x])
		soma += n
	media = soma / len(valores)
	sequencia_strings.append(string)
	if media < ssp/2: break
	lista_medias.append(media)

''' Agora, para achar a maior média, crio uma variável (MAIOR) a qual recebe
o primeiro valor da lista de médias e vai comparando com os outros da lista 
de médias, e a medida que achar um valor maior, atualiza a variável.'''

if cont > 1:
	for x in range(len(lista_medias)):
		if lista_medias[x] > ssp:
			print(sequencia_strings[x])

####
# user: fabio.araujo.leite.medeiros@ccc.ufcg.edu.br
# group: 22.1
# mode: lista5
# open_datetime: 2022-12-20T18:04:12.854188
# create_datetime: 2022-12-20T18:04:12.854188
# revision: 1
# activity: 5843614150164480
# assignment: 4678969355927552
# ip: 2804:7f7:2481:db91:fffb:2a85:94bd:897d
# timestamp: 2804:7f7:2481:db91:fffb:2a85:94bd:897d
