media = int(input())
lista = []

while True:

    delegacia = input().split()
    
    if delegacia[0] == "fim":

        for i in lista:
            print(i)

        break
    
    else:

        for i in delegacia:

            if int(i) > media:
                lista.append(i)

####
# user: steylor.barros@ccc.ufcg.edu.br
# group: 21.1e
# mode: None
# open_datetime: 2022-02-25T14:00:30.897126
# create_datetime: 2022-02-25T14:00:30.897126
# revision: 1
# activity: 5219602246139904
# assignment: 5867049555329024
# ip: 177.73.200.85
# timestamp: 177.73.200.85
