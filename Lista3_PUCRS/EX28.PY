#EX28: Escreva um algoritmo que lê um valor n inteiro e positivo e que calcula a seguinte soma:
#S := 1 + 1/2 + 1/3 + 1/4 + ... + 1/n
#O algoritmo deve escrever cada termo gerado e o valor final de S.

# Ler o valor de n
n = int(input("Digite um valor inteiro e positivo para n: "))

# Inicializar a variável de soma
soma = 0.0

# Realizar a soma dos termos da série
for i in range(1, n + 1):
    termo = 1.0 / i
    soma += termo
    print(f"Termo {i}: {termo:.4f}")

print(f"Valor final de S: {soma:.4f}")
