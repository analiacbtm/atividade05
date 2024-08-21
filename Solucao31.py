media_ssp = float(input())

n = 0
while True:
    entrada = input()
    nums = entrada.split() 
    if entrada == 'fim': break
    soma = 0
    cont = 0
    media = 0
    for i in range(len(nums)):
        soma += int(nums[i])
        cont += 1   
        media = soma / cont   
    if media < (media_ssp / 2):
        break
    if media > media_ssp:
        print(entrada)


####
# user: david.leonam.holanda@ccc.ufcg.edu.br
# group: 21.2
# mode: None
# open_datetime: 2022-08-04T11:13:27.977067
# create_datetime: 2022-08-04T11:13:27.977067
# revision: 1
# activity: 5843614150164480
# assignment: 4570108733161472
# ip: 177.73.204.219
# timestamp: 177.73.204.219
