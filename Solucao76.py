# UFCG - UNIVERSIDADE FEDERAL DE CAMPINA GRANDE
# PROGRAMAÇÃO 1 // LAB.PROG 1
# IURY BARBOSA ALVES
# CIENCIA DA COMPUTAÇÃO 2021.2

# Acima da média (Criminalidade) // UNIDADE 5 : 5786705833492480

# SOLUÇÃO


media = float(input())

# Variável criada para atribuir o valor de ocorrencia
soma = 0
# Variável criada para receber qual a última ocorrenci passada pela média
valor = []

while True:
    
    # Valores das ocorrencia em um array
    ocorrenciaDia = input().split()
    
    # Se fim, sair
    if ocorrenciaDia[0] == 'fim': 
        break
    
    # Pegamos o tamanho do array e vamos transformar eles em int e aproveitar para adicionar os valores
    for i in range(len(ocorrenciaDia)):
        soma += int(ocorrenciaDia[i])
    # Aqui pegamos a média de ocorrencia
    novaMedia = soma / len(ocorrenciaDia)
    
    # Caso a sequencia de valores cuja média seja 2 vezes menor, ele sairá
    if (novaMedia*2) < media:
        break
    elif novaMedia > media:
    # Atribuimos o valor de soma a 0.
        soma = 0
        #Atribuimos o ocorrencia a variavel valor.
        valorFormatado = ' '.join(ocorrenciaDia)
        valor.append(valorFormatado)
    else:
        soma = 0

for valores in valor:
    print(valores)
####
# user: iury.alves@ccc.ufcg.edu.br
# group: 21.2
# mode: None
# open_datetime: 2022-06-14T15:38:25.883938
# create_datetime: 2022-06-14T15:38:25.883938
# revision: 2
# activity: 5843614150164480
# assignment: 5786705833492480
# ip: 177.37.146.62
# timestamp: 177.37.146.62
