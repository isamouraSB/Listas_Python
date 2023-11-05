#EX11: Faça um programa que leia um código numérico inteiro e uma lista de 15
#posições de números reais. Se o código for zero, termine o programa. Se o
#código for 1, mostre a lista na ordem direta. Se o código for 2, mostre a lista
#na ordem inversa.

# Inicialize a lista de números reais
numeros = []

# Preencha a lista com 15 números
for i in range(15):
    numero = float(input(f"Digite o {i+1}º número real: "))
    numeros.append(numero)

while True:
    codigo = int(input("Digite o código (0 para sair, 1 para ordem direta, 2 para ordem inversa): "))
    
    if codigo == 0:
        break
    elif codigo == 1:
        # Mostrar a lista na ordem direta
        print("Lista na ordem direta:")
        for numero in numeros:
            print(numero)
    elif codigo == 2:
        # Mostrar a lista na ordem inversa
        print("Lista na ordem inversa:")
        for numero in reversed(numeros):
            print(numero)
    else:
        print("Código inválido. Tente novamente.")
