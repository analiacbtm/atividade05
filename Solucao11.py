def media_mensal(ocorrencias):
    soma = 0
    quant = 0

    for token in ocorrencias.split():
        soma += int(token)
        quant += 1

    media = soma / quant
    return media

def __main__():
    media_ssp = float(input())
    acima_da_media = []

    while True:
        ocorrencias = input()

        if ocorrencias == "fim": break

        media_delegacia = media_mensal(ocorrencias)

        if media_delegacia * 2 <= media_ssp: break

        if media_delegacia > media_ssp:
            acima_da_media.append(ocorrencias)

    for i in range(len(acima_da_media)):
        print(acima_da_media[i])


if __name__ == __main__():
    __main__
####
# user: andre.neves@ccc.ufcg.edu.br
# group: 21.2
# mode: None
# open_datetime: 2022-06-29T17:54:57.271917
# create_datetime: 2022-06-29T17:54:57.271917
# revision: 3
# activity: 5843614150164480
# assignment: 6067495729364992
# ip: 177.37.147.115
# timestamp: 177.37.147.115
