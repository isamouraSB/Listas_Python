#EX15: Escrever um algoritmo que leia uma quantidade desconhecida de números e conte quantos deles estão nos seguintes intervalos: [0.25], [26,50], [51,75] e [76,100]. A entrada de dados deve terminar quando for lido um número negativo.

# Inicializando contadores
cont_0_25 = 0
cont_26_50 = 0
cont_51_75 = 0
cont_76_100 = 0

while True:
    # Lendo o número
    num = float(input("Digite um número: "))
    
    # Verificando se o número é negativo
    if num < 0:
        break
    
    # Verificando em qual intervalo o número se encontra
    if 0 <= num <= 25:
        cont_0_25 += 1
    elif 26 <= num <= 50:
        cont_26_50 += 1
    elif 51 <= num <= 75:
        cont_51_75 += 1
    elif 76 <= num <= 100:
        cont_76_100 += 1

# Imprimindo os resultados
print("Quantidade de números no intervalo [0,25]: ", cont_0_25)
print("Quantidade de números no intervalo [26,50]: ", cont_26_50)
print("Quantidade de números no intervalo [51,75]: ", cont_51_75)
print("Quantidade de números no intervalo [76,100]: ", cont_76_100)
