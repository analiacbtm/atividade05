mediaMensal = float(input())
sequencias = ''

while True:
    valores = input()
    
    if(valores == 'fim'): break
    
    soma  = 0
    quant = 0

    for valor in valores.split():
        
        soma += float(valor)
        quant += 1

    media = soma / quant

    if((media * 2) <= mediaMensal): break

    if(media > mediaMensal):
        sequencias +=  valores + ';'


for sequencia in sequencias.split(';'):
    if sequencia != '':    
        print(sequencia)
####
# user: joao.victor.oliveira@ccc.ufcg.edu.br
# group: 21.1e
# mode: None
# open_datetime: 2022-02-13T21:32:48.478744
# create_datetime: 2022-02-13T21:32:48.478744
# revision: 1
# activity: 5219602246139904
# assignment: 5853308981870592
# ip: 45.236.70.198
# timestamp: 45.236.70.198
