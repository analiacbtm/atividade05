media = float(input())

while True:
    seq = input()
    if seq == "fim": break
    seq_final = seq.split(' ')
    num_geral = 0 
    
    for i in seq_final:
        num_geral += int(i)
    med = num_geral / len(seq_final)
    
    if med * 2 < media: break
    
    if med > media:
        print(seq)
####
# user: julio.cesar.silva.alcantara@ccc.ufcg.edu.br
# group: 22.1
# mode: None
# open_datetime: 2022-12-04T17:01:44.154380
# create_datetime: 2022-12-04T17:01:44.154380
# revision: 1
# activity: 5843614150164480
# assignment: 5280050549096448
# ip: 2804:6888:e688:1:2f20:715a:45f8:af13
# timestamp: 2804:6888:e688:1:2f20:715a:45f8:af13
