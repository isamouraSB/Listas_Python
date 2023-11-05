#EX31: Escrever um algoritmo que lê 10 valores, um de cada vez, e conta quantos deles estão no intervalo [10,20] e quantos deles estão fora do intervalo, escrevendo estas informações

# Inicializando contadores
cont_intervalo = 0
cont_fora_intervalo = 0

for i in range(10):
    # Lendo o valor
    valor = float(input("Digite um valor: "))
    
    # Verificando se o valor está no intervalo [10,20]
    if 10 <= valor <= 20:
        cont_intervalo += 1
    else:
        cont_fora_intervalo += 1

# Imprimindo as informações
print(f"Quantidade de valores no intervalo [10,20]: {cont_intervalo}")
print(f"Quantidade de valores fora do intervalo [10,20]: {cont_fora_intervalo}")
