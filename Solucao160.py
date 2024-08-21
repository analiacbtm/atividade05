#FUNÇÕES:
def t_media(seq, media_ssp):
    tot = 0
    for i in range(len(seq)):
        tot += int(seq[i])
        media = tot/len(seq)
    if (media_ssp/2) < media:
        return media, 'continuar'
    else:
        return media, 'parar'

#ATRIBUIÇÕES:
entrada = ''
seq = []
media_ssp = float(input())
maiores = []

while entrada != 'fim':
    seq =[]
    entrada = input()
    if entrada == 'fim':
        break
    else:
        seq = entrada.split()
        valor_media, teste_media = t_media(seq, media_ssp)
        if valor_media > media_ssp:
            maiores.append(seq)
        if teste_media == 'continuar':
            continue
        else:
            break
#SAÍDAS
for i in range (len(maiores)):
    for j in range(len(maiores[i])):
        if j == (len(maiores[i]))-1:
            print(int(maiores[i][j]))
        else:
            print(int(maiores[i][j]), end =' ')
####
# user: vitor.marinho.magliano@ccc.ufcg.edu.br
# group: 22.1
# mode: None
# open_datetime: 2022-11-09T02:22:52.974337
# create_datetime: 2022-11-09T02:22:52.974337
# revision: 1
# activity: 5843614150164480
# assignment: 5336546095923200
# ip: 181.223.165.238
# timestamp: 181.223.165.238
