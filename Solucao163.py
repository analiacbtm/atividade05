#criminal
def media_sequencia(seq):
    soma = 0
    for v in seq:
        soma += v
    media = soma / len(seq)
    return media

limite = float(input())


linhas = []
while True:
    dados = input()
    if dados == 'fim': break
    
    token = dados.split()
    sequencia = [int(v) for v in token]
    media = media_sequencia(sequencia)
    if media < limite / 2: break
    if media > limite:
        linhas.append(sequencia)

for x in linhas:
    for y in range(len(x) - 1):
        print(x[y], end=' ')
    print(x[len(x) - 1])
    
####
# user: wendell.tome.marinho.oliveira@ccc.ufcg.edu.br
# group: 22.1
# mode: None
# open_datetime: 2022-11-09T00:43:02.432933
# create_datetime: 2022-11-09T00:43:02.432933
# revision: 3
# activity: 5843614150164480
# assignment: 6495801188548608
# ip: 45.6.36.50
# timestamp: 45.6.36.50
