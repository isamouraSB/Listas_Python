#EX21: Faça um algoritmo que leia vários números inteiros e positivos e calcule o produtório dos números pares. O fim da leitura será indicado pelo número 0.

produtorio_pares = 1

while True:
    numero = int(input("Digite um número (ou 0 para sair): "))
    
    if numero == 0:
        break

    if numero % 2 == 0:
        produtorio_pares *= numero

print(f"Produtório dos números pares: {produtorio_pares}")

