# Disciplina: laboratório de programação e programação.
# Aluno: Lucas de Lima da Silva.
# Matrícula: 121110517.
# Objetivo: um programa que leia a média mensal estabelecida pela secretaria de segurança pública e várias sequencias de valores que representam a quantidade de ocorrências registradas por dia na delegacia. O programa deve imprimir na saída apenas as sequências cuja média mensal é maior que o estabelecido.

condi = 0
while condi == 0 : 
    medssp = float(input())
    while True:
        l = ''
        result = []
        sui = 0
        sequencia = input().split()
        if sequencia[0] == 'fim':
            condi += 1
            break
        soma = 0
        for ini in range(len(sequencia)):
            l += sequencia[ini]
            if (len(sequencia) - 1) > sui:
                l += ' '
                sui += 1
            ini = int(sequencia[ini])
            result.append(ini)
            soma += ini
        media = soma / len(sequencia)
        if media < (medssp / 2): 
            break  
        if media > medssp:
            print(l)
    condi += 1

####
# user: lucas.lima.silva@ccc.ufcg.edu.br
# group: 21.1e
# mode: None
# open_datetime: 2022-03-09T18:48:58.888779
# create_datetime: 2022-03-09T18:48:58.888779
# revision: 1
# activity: 5219602246139904
# assignment: 5803555745169408
# ip: 177.84.220.37
# timestamp: 177.84.220.37
