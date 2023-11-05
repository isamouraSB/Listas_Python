#EX17: Escrever um algoritmo que lê um número não determinado de pares de valores m,n, todos inteiros e positivos, um par de cada vez, e calcula e escreve a soma dos n inteiros consecutivos a partir de m inclusive.


while True:
    # Lendo os valores de m e n
    m = input("Digite o valor de m (ou 'sair' para terminar): ")
    
    # Verificando se o usuário quer sair
    if m.lower() == 'sair':
        break
    
    # Convertendo m para inteiro
    m = int(m)
    
    n = int(input("Digite o valor de n: "))
    
    # Verificando se m e n são positivos
    if m < 0 or n < 0:
        print("Por favor, digite apenas valores inteiros e positivos.")
        continue
    
    # Calculando a soma dos n inteiros consecutivos a partir de m
    soma = sum(range(m, m + n))
    
    # Imprimindo a soma
    print(f"A soma dos {n} inteiros consecutivos a partir de {m} é {soma}.")
