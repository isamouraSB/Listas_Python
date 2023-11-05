#EX7:Escreva um programa que leia e mostre uma lista de 10 elementos inteiros. Em seguida, conte quantos valores pares existem na lista, por fim, exiba a quantidade na tela.

# Inicialize uma lista vazia para armazenar os elementos
lista = []

# Faça um loop para ler 10 elementos inteiros
for i in range(10):
    elemento = int(input(f"Digite o {i+1}º elemento: "))
    lista.append(elemento)

# Inicialize uma variável para contar os valores pares
contagem_pares = 0

# Faça um loop para percorrer a lista e contar os valores pares
for elemento in lista:
    if elemento % 2 == 0:
        contagem_pares += 1

# Exiba a quantidade de valores pares na lista
print(f"A quantidade de valores pares na lista é: {contagem_pares}")
