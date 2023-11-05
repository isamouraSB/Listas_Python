#EX19: Faça um algoritmo que leia uma quantidade não determinada de números positivos. Calcule a quantidade de números pares e ímpares, a média de valores pares e a média geral dos números lidos. O número que encerrará a leitura será zero.


soma_pares = 0
soma_impares = 0
contagem_pares = 0
contagem_geral = 0

while True:
    numero = int(input("Digite um número (ou 0 para sair): "))
    
    if numero == 0:
        break

    contagem_geral += 1
    if numero % 2 == 0:
        soma_pares += numero
        contagem_pares += 1
    else:
        soma_impares += numero

if contagem_pares > 0:
    media_pares = soma_pares / contagem_pares
else:
    media_pares = 0

if contagem_geral > 0:
    media_geral = (soma_pares + soma_impares) / contagem_geral
else:
    media_geral = 0

print(f"Quantidade de números pares: {contagem_pares}")
print(f"Quantidade de números ímpares: {contagem_geral - contagem_pares}")
print(f"Média de valores pares: {media_pares}")
print(f"Média geral: {media_geral}")
