#EX9: Escreva um algoritmo que leia 50 valores e encontre o maior e o menor deles. Mostre o resultado.

valores = [float(input(f"Digite o valor {i+1}: ")) for i in range(50)]
maior = max(valores)
menor = min(valores)
print(f"O maior valor digitado foi {maior} e o menor foi {menor}.")
