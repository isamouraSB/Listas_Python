#EX1: Escrever um algoritmo que lê 5 valores para a, um de cada vez, e conta quantos destes valores são negativos, escrevendo esta informação.

contagem_negativos = 0

for i in range(5):
    a = float(input("Digite um valor para a: "))
    if a < 0:
        contagem_negativos += 1

print(f"Quantidade de valores negativos: {contagem_negativos}")
