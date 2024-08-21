media_mensal = float(input())

lista_de_medias = []

while True:
    ocorrencias = input()
    
    if ocorrencias == "fim":
        break

    ocorrencias = ocorrencias.split()

    soma = 0
    for num in ocorrencias:
        soma += int(num)

    media = soma / len(ocorrencias)

    if media > media_mensal:
        texto = ""
        for i in range(len(ocorrencias)):
            if i == len(ocorrencias) - 1:
                texto += ocorrencias[i]
            else:
                texto += ocorrencias[i] + " "
        
        lista_de_medias.append(texto)
    
    if media < (media_mensal / 2):
        break

for t in lista_de_medias:
    print(t)

    
        
####
# user: sergio.gustavo.andrade.grilo@ccc.ufcg.edu.br
# group: 22.1
# mode: None
# open_datetime: 2022-11-07T19:58:10.137342
# create_datetime: 2022-11-07T19:58:10.137342
# revision: 1
# activity: 5843614150164480
# assignment: 6023659929993216
# ip: 2804:29b8:505c:9108:81b2:aca1:51cd:89d0
# timestamp: 2804:29b8:505c:9108:81b2:aca1:51cd:89d0
