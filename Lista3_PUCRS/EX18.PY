#EX18: Escrever um algoritmo que lê um número não determinado de valores para m, todos inteiros e positivos, um de cada vez. Se m for par, verificar quantos divisores possui e escrever esta informação. Se m for ímpar e menor do que 10 calcular e escrever o fatorial de m. Se m for ímpar e maior ou igual a 10 calcular e escrever a soma dos inteiros de 1 até m.

import math

while True:
    # Lendo o valor de m
    m = input("Digite o valor de m (ou 'sair' para terminar): ")
    
    # Verificando se o usuário quer sair
    if m.lower() == 'sair':
        break
    
    # Convertendo m para inteiro
    m = int(m)
    
    # Verificando se m é positivo
    if m < 0:
        print("Por favor, digite apenas valores inteiros e positivos.")
        continue
    
    # Verificando se m é par
    if m % 2 == 0:
        # Calculando a quantidade de divisores de m
        divisores = [i for i in range(1, m + 1) if m % i == 0]
        print(f"O número {m} possui {len(divisores)} divisores.")
    else:
        # Verificando se m é menor do que 10
        if m < 10:
            # Calculando o fatorial de m
            fatorial = math.factorial(m)
            print(f"O fatorial de {m} é {fatorial}.")
        else:
            # Calculando a soma dos inteiros de 1 até m
            soma = sum(range(1, m + 1))
            print(f"A soma dos inteiros de 1 até {m} é {soma}.")

