#EX3: Escreva um programa que leia 10 números de reais e informe:
#a) a média dos elementos;
#b) o maior e menor elemento;
#c) a quantidade de elementos positivos e a quantidade de elementos negativos.

numeros = []
for i in range(10):
    numero = float(input("Digite um número real: "))
    numeros.append(numero)

media = sum(numeros) / len(numeros)
maior = max(numeros)
menor = min(numeros)
positivos = len([num for num in numeros if num > 0])
negativos = len([num for num in numeros if num < 0])

print(f"A média dos elementos é {media}")
print(f"O maior elemento é {maior} e o menor elemento é {menor}")
print(f"A quantidade de elementos positivos é {positivos} e a quantidade de elementos negativos é {negativos}")
