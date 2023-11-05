#EX20: Faça um algoritmo que leia vários números inteiros e calcule o somatório dos números negativos. O fim da leitura será indicado pelo número 0.

soma_negativos = 0

while True:
    numero = int(input("Digite um número (ou 0 para sair): "))
    
    if numero == 0:
        break

    if numero < 0:
        soma_negativos += numero

print(f"Somatório dos números negativos: {soma_negativos}")
