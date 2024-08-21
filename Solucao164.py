# Meses que a media de ocorrencias / dia for maior que a media da ssp
# Lê a média mensal e a sequencia de ocorrencias

lista = []
media = soma = 0
media_ssp = float(input())

while True:
    soma = media = 0

    sequencia = input()
    if sequencia == 'fim':
        break
    sequencia = sequencia.split()
    
    for i in range(len(sequencia)): # Convert to integer
        sequencia[i] = int(sequencia[i])
    
    for n in sequencia:
        soma += n
        media = soma / len(sequencia)

    if media < media_ssp / 2:
        break
    
    if media > media_ssp:
        lista.append(sequencia)

# Output
res = ''
for seq in lista:
    for j in range(len(seq)):
        if j == len(seq) - 1:
            print(seq[j])
        else:
            print(seq[j], end=' ')

####
# user: winicius.allan.bezerra.silva@ccc.ufcg.edu.br
# group: 22.1
# mode: None
# open_datetime: 2022-11-21T13:36:06.920564
# create_datetime: 2022-11-21T13:36:06.920564
# revision: 1
# activity: 5843614150164480
# assignment: 5610679815897088
# ip: 150.165.42.205
# timestamp: 150.165.42.205
