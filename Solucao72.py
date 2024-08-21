def main():
    registros = []

    media_ssp = float(input())

    while True:
        registro = input()
        valores = registro.split()

        if registro == "fim" or media(valores) * 2 <= media_ssp:
            break
        else:
            if media(valores) > media_ssp:
                registros.append(registro)

    for linha in registros:
        print(linha)


def media(lista):
    soma = 0

    for item in lista:
        soma += int(item)

    return soma / len(lista)


if __name__ == "__main__":
    main()
####
# user: isaac.vicente.medeiros.silva@ccc.ufcg.edu.br
# group: 22.1
# mode: None
# open_datetime: 2022-11-09T18:59:30.690364
# create_datetime: 2022-11-09T18:59:30.690364
# revision: 3
# activity: 5843614150164480
# assignment: 6413117632282624
# ip: 189.105.25.190
# timestamp: 189.105.25.190
