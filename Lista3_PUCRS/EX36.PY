#EX36: Escrever um algoritmo que leia um número N que indica quantos valores devem ser lidos a seguir. Para cada número lido, mostre uma tabela contendo o valor lido e o fatorial deste valor.

# Função para calcular o fatorial de um número
def fatorial(numero):
    if numero == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, numero + 1):
            resultado *= i
        return resultado

# Ler o número N
N = int(input("Digite o número de valores a serem lidos: "))

# Loop para ler os valores e mostrar a tabela
print("Valor | Fatorial")
for _ in range(N):
    valor = int(input("Digite um valor: "))
    resultado_fatorial = fatorial(valor)
    print(f"{valor}    | {resultado_fatorial}")

