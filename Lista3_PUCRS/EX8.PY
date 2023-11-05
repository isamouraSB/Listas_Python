#EX8: Escreva um algoritmo que calcule a média dos números digitados pelo usuário, se eles forem pares. Termine a leitura se o usuário digitar zero (0).

numeros_pares = []

while True:
    numero = int(input("Digite um número (0 para sair): "))
    if numero == 0:
        break
    if numero % 2 == 0:
        numeros_pares.append(numero)

if numeros_pares:
    media = sum(numeros_pares) / len(numeros_pares)
    print(f"A média dos números pares digitados é {media:.2f}")
else:
    print("Nenhum número par foi digitado.")
