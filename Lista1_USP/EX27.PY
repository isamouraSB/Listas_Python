#EX27: Foi feita uma pesquisa de audiência de canal de TV em várias casas de uma cidade, em um determinado dia. Para cada casa consultada foi fornecido o número do canal (4, 5, 7, 12) e o número de pessoas que estavam assistindo àquele canal. Se a televisão estivesse desliga- da, nada era anotado, ou seja, essa casa não entrava na pesquisa. Faça um programa que:
#a) leia um número indeterminado de dados (número do canal e o número de pessoas que estavam assistindo);
#b) calcule e mostre a percentagem de audiência de cada canal.
#Para encerrar a entrada de dados digite o número do canal ZERO.

# Inicializando as variáveis
audiencia_canal = {4: 0, 5: 0, 7: 0, 12: 0}
total_pessoas = 0

# Coletando os dados
while True:
    canal = int(input("Digite o número do canal (ou 0 para sair): "))
    if canal == 0:
        break
    pessoas = int(input("Digite o número de pessoas que estavam assistindo: "))
    if canal in audiencia_canal:
        audiencia_canal[canal] += pessoas
    total_pessoas += pessoas

# Calculando e mostrando a percentagem de audiência de cada canal
for canal, audiencia in audiencia_canal.items():
    percentagem_audiencia = (audiencia / total_pessoas) * 100 if total_pessoas > 0 else 0
    print("Percentagem de audiência do canal", canal, ":", percentagem_audiencia)
