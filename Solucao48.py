media_ssp = float(input())

while True:
    media_ocor = input()
    
    if media_ocor == "fim":
        break

    verf = media_ocor.split()
    soma = 0
    
    for num in verf:
        soma += int(num)
    
    media = soma / len(verf)
    
    if media < (media_ssp / 2):
        break
    
    if media > media_ssp:
        print(media_ocor)
####
# user: filipe.luiz.lino.azevedo@ccc.ufcg.edu.br
# group: 22.1
# mode: None
# open_datetime: 2022-11-07T20:13:14.536415
# create_datetime: 2022-11-07T20:13:14.536415
# revision: 4
# activity: 5843614150164480
# assignment: 4947882291494912
# ip: 2804:389:7102:1bb4:c3a5:6408:f5f2:2eaa
# timestamp: 2804:389:7102:1bb4:c3a5:6408:f5f2:2eaa
