# Universidade Federal de Campina Grande
# Ciência da Computação - Programação 1

# Vitória Maria do Nascimento - 2021.2

# Questão: "Criminalidade" - Unidade: 5

def transforma_em_inteiros(valores_processados):
    lista = []
    for ele in (valores_processados.split()):
        if ele != 'fim':
            lista.append(int(ele))
    return lista


def calcula_menor_media(lista):

    media = 0
    for ele in lista:
        media += ele

    media_menor = media / len(lista)

    return media_menor


def main():

    media_mensal = float(input())
    maior_media = ''

    while True:

        valores_processados = input()

        if valores_processados == 'fim':
            break

        lista = transforma_em_inteiros(valores_processados)
        media_menor = calcula_menor_media(lista)

        if media_menor < (media_mensal / 2):
            break

        if media_menor > media_mensal:
            maior_media += valores_processados
            maior_media += '\n'

    print(f'{maior_media}' , end='')

if __name__ == '__main__':
    main()
####
# user: vitoria.nascimento@ccc.ufcg.edu.br
# group: 21.2
# mode: None
# open_datetime: 2022-07-25T20:50:24.419844
# create_datetime: 2022-07-25T20:50:24.419844
# revision: 4
# activity: 5843614150164480
# assignment: 5580283510259712
# ip: 177.73.206.93
# timestamp: 177.73.206.93
