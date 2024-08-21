def calculaMedia(valores):

    mediaMensal = 0
    for i in valores:
        mediaMensal += int(i)

    mediaMensal = mediaMensal/len(valores)

    return mediaMensal

def main():
    mediaPadrao = float(input())

    listaMediasMensais = []
    while True:
        linha = input()
        if linha == 'fim': break

        valores = linha.split()
        mediaMensal = calculaMedia(valores)

        if mediaPadrao < mediaMensal:
            listaMediasMensais.append(linha)
        elif mediaMensal < (mediaPadrao/2): break

    
    for i in listaMediasMensais:
        print(i)

    

main()
    
####
# user: alexandre.souto.medeiros@ccc.ufcg.edu.br
# group: 21.2
# mode: None
# open_datetime: 2022-07-04T14:01:37.072446
# create_datetime: 2022-07-04T14:01:37.072446
# revision: 1
# activity: 5843614150164480
# assignment: 4546945370554368
# ip: 2804:29b8:505a:50d8:34aa:da8f:63d1:7322
# timestamp: 2804:29b8:505a:50d8:34aa:da8f:63d1:7322
