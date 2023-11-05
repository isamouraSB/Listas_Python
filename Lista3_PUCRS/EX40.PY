#EX40: Escrever um algoritmo que lê um valor n que indica quantos valores devem ser lidos para m, valores inteiros e positivos, com leitura de um valor de cada vez. Escreva
#uma tabela contendo o valor lido, o somatório dos inteiros de 1 até m e o fatorial de m.

# Função para calcular o fatorial de um número
def fatorial(numero):
    if numero == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, numero + 1):
            resultado *= i
        return resultado

# Ler o valor n
n = int(input("Digite o valor de n: "))

# Loop para ler os valores m e mostrar a tabela
print("Valor m | Somatório | Fatorial")
for _ in range(n):
    m = int(input("Digite o valor de m: "))
    somatorio = sum(range(1, m + 1))
    fatorial_m = fatorial(m)
    print(f"{m}         | {somatorio}           | {fatorial_m}")
