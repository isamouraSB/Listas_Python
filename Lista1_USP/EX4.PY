# EX4: Faça um programa que leia cinco grupos de quatro valores (A, D, C, D) e mostre-os na ordem lida, Em seguida mostre-os em ordem crescente e decrescente; 

# Função para ler os valores
def ler_valores():
    grupos = []
    for i in range(5):
        print(f"Insira os valores para o grupo {i+1}:")
        A = int(input("Insira o valor para A: "))
        B = int(input("Insira o valor para B: "))
        C = int(input("Insira o valor para C: "))
        D = int(input("Insira o valor para D: "))
        grupos.append([A, B, C, D])
    return grupos

# Função para imprimir os valores
def imprimir_valores(grupos):
    print("\nValores na ordem lida:")
    for i in range(5):
        print(f"Grupo {i+1}: {grupos[i]}")

    print("\nValores em ordem crescente:")
    for i in range(5):
        print(f"Grupo {i+1}: {sorted(grupos[i])}")

    print("\nValores em ordem decrescente:")
    for i in range(5):
        print(f"Grupo {i+1}: {sorted(grupos[i], reverse=True)}")

# Programa principal
def main():
    grupos = ler_valores()
    imprimir_valores(grupos)

# Executar o programa principal
if __name__ == "__main__":
    main()
