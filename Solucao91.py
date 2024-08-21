media = float(input())
melhor_dia = []
melhor_media = 0.0
while True:
    dia_str = input()
    if(dia_str == "fim"):
        break
    dia_int = [int(x) for x in dia_str.split(" ")]
    media_diaria = 0
    for y in dia_int:
        media_diaria += y
    media_diaria = media_diaria/len(dia_int)

    if(media_diaria < media/2):
        break
    
    elif(media_diaria > media):
        melhor_dia.append(dia_str)

for z in melhor_dia:
    print(z)
####
# user: kayky.fidelis.serafim@ccc.ufcg.edu.br
# group: 22.1
# mode: None
# open_datetime: 2022-11-21T13:14:53.128422
# create_datetime: 2022-11-21T13:14:53.128422
# revision: 2
# activity: 5843614150164480
# assignment: 6139453590470656
# ip: 150.165.42.209
# timestamp: 150.165.42.209
