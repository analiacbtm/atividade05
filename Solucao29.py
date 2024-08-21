def converte_int(sequencia):
    nova = []
    for i in range(len(sequencia)):
        valor = int(sequencia[i])
        nova.append(valor)

    return nova


def soma(valores):
    soma = 0
    for v in valores:
        soma += v 

    return soma 


def imprimir(lista_composta):
    for l in lista_composta:
        for i in range(len(l)):
            if (i != (len(l) - 1)):
                print(l[i], end=' ')
            else:
                print(l[i])
        

def main():
    media = float(input())
    lista_maiores = []
    while True:
        sequencia = input().split()
        if sequencia == ['fim']: 
            break
        sequencia = converte_int(sequencia)
        media_sequencia = float(soma(sequencia) / len(sequencia))
        if (2 * media_sequencia) < media:
            break
        
        if (media_sequencia) > media:
            lista_maiores.append(sequencia)

    imprimir(lista_maiores)


if __name__ == '__main__':
    main()####
# user: david.goncalves.silva@ccc.ufcg.edu.br
# group: 21.2
# mode: None
# open_datetime: 2022-07-05T03:56:05.042776
# create_datetime: 2022-07-05T03:56:05.042776
# revision: 1
# activity: 5843614150164480
# assignment: 5994542824161280
# ip: 2804:29b8:505e:47be:9d12:90f3:da09:b4f5
# timestamp: 2804:29b8:505e:47be:9d12:90f3:da09:b4f5
