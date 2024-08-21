media_ssp = float(input())

lista_de_sequencias_validas = []


while True:
    soma = media = 0
    sequencia = input().split()
    
    if sequencia[0] != 'fim':
        for num in sequencia:
            soma += float(num)
    
    if soma != 0:
        media = soma / len(sequencia)
    
    if media > media_ssp:
        lista_de_sequencias_validas.append(sequencia)
    elif sequencia[0] == 'fim' or media < media_ssp / 2: break

for sequencia in lista_de_sequencias_validas:
    resposta = ''
    for num in range(len(sequencia)):

        if num != len(sequencia) - 1:
            resposta += sequencia[num] + " "
        else:
            resposta += sequencia[num]
    print(resposta)
####
# user: sabrina.silva@ccc.ufcg.edu.br
# group: 21.1e
# mode: None
# open_datetime: 2022-02-12T02:34:03.376793
# create_datetime: 2022-02-12T02:34:03.376793
# revision: 1
# activity: 5219602246139904
# assignment: 5312386305097728
# ip: 2804:29b8:507a:244c:29cb:af88:621d:924
# timestamp: 2804:29b8:507a:244c:29cb:af88:621d:924
