def imprime_lista(lista):
	linha = ''
	for x in range(len(lista)):
		linha += str(lista[x])
		if x < len(lista) - 1:
			linha += ' '
	return linha

def avalia_registros(limite,lista):
	media_lista = sum(lista) / len(lista)
	if media_lista > limite:
		return True


def media_diaria(lista):
	media = sum(lista) / len(lista)
	return media
	

def str_to_int(lista):
	for x in range(len(lista)):
		lista[x] = int(lista[x])
	return lista


def le_ocorrencias(limite):
	over = []
	while True:
		ocorrencias_str = input()
		if ocorrencias_str == 'fim': 
			return over
			break
		
		ocorrencias_str = ocorrencias_str.split()
		ocorrencias = str_to_int(ocorrencias_str)
		media = media_diaria(ocorrencias)
		
		if 	(limite/2) > media:
			return over
		
		if avalia_registros(limite,ocorrencias):
		
			over.append(ocorrencias_str)
				
def main():
	limite = float(input())
	resultado = le_ocorrencias(limite)
	if resultado != None: 
		for x in range(len(resultado)):
			print(imprime_lista(resultado[x]))
main()
####
# user: pedro.braz@ccc.ufcg.edu.br
# group: 21.2
# mode: None
# open_datetime: 2022-06-30T01:01:57.639583
# create_datetime: 2022-06-30T01:01:57.639583
# revision: 3
# activity: 5843614150164480
# assignment: 5435936290635776
# ip: 2804:d49:6f04:d400:7d5e:cadf:ee6e:eff2
# timestamp: 2804:d49:6f04:d400:7d5e:cadf:ee6e:eff2
