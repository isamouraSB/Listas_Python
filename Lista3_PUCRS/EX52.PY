#EX52: Faça um algoritmo que calcule a combinação e arranjo de um conjunto de tamanho N em subconjuntos de p elementos.


# Função para calcular o fatorial de um número
def calcular_fatorial(numero):
    if numero == 0:
        return 1
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
    return fatorial

# Função para calcular a combinação (C)
def calcular_combinacao(n, p):
    if p > n:
        return 0
    return calcular_fatorial(n) // (calcular_fatorial(p) * calcular_fatorial(n - p))

# Função para calcular o arranjo (A)
def calcular_arranjo(n, p):
    if p > n:
        return 0
    return calcular_fatorial(n) // calcular_fatorial(n - p)

# Ler os valores de N e p
n = int(input("Digite o valor de N: "))
p = int(input("Digite o valor de p: "))

# Calcular e exibir a combinação e o arranjo
combinacao = calcular_combinacao(n, p)
arranjo = calcular_arranjo(n, p)

print(f"Combinação de C({n}, {p}) = {combinacao}")
print(f"Arranjo de A({n}, {p}) = {arranjo}")

