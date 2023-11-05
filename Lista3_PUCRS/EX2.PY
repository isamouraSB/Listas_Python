#EX2: 2. Escrever um algoritmo que lê um valor N inteiro e positivo e que calcula e escreve o valor de E.
#E = 1 + 1 / 1! + 1 / 2! + 1 / 3! + 1 / N!

# Função para calcular o fatorial de um número
def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

# Ler o valor de N
N = int(input("Digite um valor inteiro e positivo N: "))

# Inicializar o valor de E
E = 1.0  # Começa com o primeiro termo da série (1/0!)

# Calcular a soma da série
for i in range(1, N + 1):
    termo = 1 / fatorial(i)  # Calcula o próximo termo da série
    E += termo

# Exibir o valor de E
print(f"O valor de E para N = {N} é aproximadamente {E:.6f}")
