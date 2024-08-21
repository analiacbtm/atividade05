media = float(input())


while True:
    sequencia = input().split()
    i = 0
    soma = 0
    if sequencia[i] == 'fim': break
    
    for i in range(len(sequencia)):
        
        soma =(soma + int(sequencia[i]))

    media_sequencia = soma / len(sequencia)
    
    if media_sequencia * 2 < media: break


    if media_sequencia > media:

        for i in range(len(sequencia)):

            if i == len(sequencia) - 1:
                print(f'{sequencia[i]}')
            else:    
                print(f'{sequencia[i]}', end=" ")

    
####
# user: nouasse.ben@ccc.ufcg.edu.br
# group: 21.2
# mode: None
# open_datetime: 2022-06-16T03:19:38.073184
# create_datetime: 2022-06-16T03:19:38.073184
# revision: 1
# activity: 5843614150164480
# assignment: 5784782174683136
# ip: 177.37.145.68
# timestamp: 177.37.145.68
