#EX49: Faça um algoritmo que lê um valor N inteiro e positivo e que calcula e escreve o fatorial de N (N!)

# Ler o valor N
N = int(input("Digite um valor inteiro e positivo para calcular o fatorial: "))

# Verificar se N é um valor válido
if N < 0:
    print("O fatorial não está definido para números negativos.")
else:
    # Inicializar o fatorial como 1
    fatorial = 1

    # Calcular o fatorial de N
    for i in range(1, N + 1):
        fatorial *= i

    # Imprimir o resultado
    print(f"{N}! = {fatorial}")
