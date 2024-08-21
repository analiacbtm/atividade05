mm = float(input())

cond = ''
out = []
while cond != 'fim':
    se = input()
    seq = se.split(' ')
    media = 0
    if seq != ['fim']:
        for i in range(len(seq)):
            seq[i] = int(seq[i])
            media += (seq[i])/(len(seq))
        if media > mm:
            out.append(se)
        if media < (mm/2):
            break
    else:
        cond = 'fim'

for v in range(len(out)):
    print(out[v])


####
# user: ana.virginia.souza.nery@ccc.ufcg.edu.br
# group: 22.1
# mode: None
# open_datetime: 2022-11-17T03:45:55.548665
# create_datetime: 2022-11-17T03:45:55.548665
# revision: 2
# activity: 5843614150164480
# assignment: 4697154918547456
# ip: 191.35.81.250
# timestamp: 191.35.81.250
