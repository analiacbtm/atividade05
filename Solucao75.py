media_estabelecida = float(input())
ocorrencias_acima = []

while True:
    sequencia_ocorrencias = input().split()
    media_ocorrencias = 0
    if sequencia_ocorrencias[0] == 'fim': break
    for i in range(len(sequencia_ocorrencias)):
        media_ocorrencias += int(sequencia_ocorrencias[i])
    media_ocorrencias = media_ocorrencias / len(sequencia_ocorrencias)
    if media_ocorrencias > media_estabelecida:
        ocorrencias_acima.append(sequencia_ocorrencias)
        media_ocorrencias = 0
    elif media_ocorrencias < media_estabelecida / 2: break
    else:
        media_ocorrencias = 0

for i in range(len(ocorrencias_acima)):
    sequencia = ocorrencias_acima[i]
    string_sequencia = ''
    for j in range(len(sequencia)):
        if j == 0:
            string_sequencia += sequencia[j]
        else:
            string_sequencia += ' '
            string_sequencia += sequencia[j]
    print(string_sequencia)
                    
####
# user: israel.silva@ccc.ufcg.edu.br
# group: 21.1e
# mode: None
# open_datetime: 2022-02-28T11:00:45.950580
# create_datetime: 2022-02-28T11:00:45.950580
# revision: 1
# activity: 5219602246139904
# assignment: 5846940518449152
# ip: 177.37.145.1
# timestamp: 177.37.145.1
