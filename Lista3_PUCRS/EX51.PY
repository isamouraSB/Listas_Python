#EX51: Faça um algoritmo que calcule o fatorial de um número.

# Função para calcular o fatorial de um número
def calcular_fatorial(n):
    if n < 0:
        return "Fatorial não está definido para números negativos"
    elif n == 0:
        return 1
    else:
        fatorial = 1
        for i in range(1, n + 1):
            fatorial *= i
        return fatorial

# Ler o número para o qual você deseja calcular o fatorial
numero = int(input("Digite um número para calcular o fatorial: "))

# Chamar a função e exibir o resultado
resultado = calcular_fatorial(numero)
print(f"{numero}! = {resultado}")
