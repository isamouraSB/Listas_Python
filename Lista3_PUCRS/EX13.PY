#EX13: Escrever um algoritmo que leia um número n que indica quantos valores devem ser lidos a seguir. Para cada número lido, mostre uma tabela contendo o valor lido e o fatorial deste valor.

# Função para calcular o fatorial de um número
def fatorial(numero):
    if numero == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, numero + 1):
            resultado *= i
        return resultado

# Ler o número n
n = int(input("Digite o número de valores a serem lidos: "))

# Loop para ler os valores e mostrar a tabela
print("Valor | Fatorial")
for i in range(n):
    valor = int(input(f"Digite o valor {i + 1}: "))
    resultado_fatorial = fatorial(valor)
    print(f"{valor}    | {resultado_fatorial}")
