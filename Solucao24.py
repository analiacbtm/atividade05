def converte(lista):
    lista_convertida = list(map(int, lista))

    return lista_convertida


def resultado(lista_media, lista_ocorrencias, media_ssp):
    for media in lista_media:
        if media > media_ssp:
            output = ' '.join(
                map(str, lista_ocorrencias[lista_media.index(media)]))
            print(output)


lista_media = []
lista_ocorrencias = []

media_ssp = float(input())

while True:
    ocorrencias = str(input())

    if ocorrencias == 'fim':
        resultado(lista_media, lista_ocorrencias, media_ssp)
        break

    lista_ocorrencias.append(converte(list(ocorrencias.split())))

    media = sum(lista_ocorrencias[-1]) / len(lista_ocorrencias[-1])
    lista_media.append(media)

    if media <= media_ssp / 2:
        resultado(lista_media, lista_ocorrencias, media_ssp)
        break
####
# user: daniel.soares@ccc.ufcg.edu.br
# group: 21.2
# mode: None
# open_datetime: 2022-06-25T00:59:18.275983
# create_datetime: 2022-06-25T00:59:18.275983
# revision: 1
# activity: 5843614150164480
# assignment: 5309089045282816
# ip: 187.19.251.77
# timestamp: 187.19.251.77
