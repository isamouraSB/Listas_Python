#EX16: Escrever um algoritmo que lê um conjunto não determinado de valores, um de cada vez, e escreve uma tabela com cabeçalho, que deve ser repetido a cada 20 linhas. A tabela conterá o valor lido, seu quadrado, seu cubo e sua raiz quadrada.

import math

# Inicialize as variáveis
linha_count = 0

while True:
    # Ler um valor
    valor = float(input("Digite um valor (ou -1 para sair): "))

    # Verifique se o usuário deseja sair
    if valor == -1:
        break

    # Verifique se é hora de imprimir o cabeçalho
    if linha_count % 20 == 0:
        print("Valor   | Quadrado  | Cubo      | Raiz Quadrada")
        print("-" * 45)

    # Calcule os valores
    quadrado = valor ** 2
    cubo = valor ** 3
    raiz_quadrada = math.sqrt(valor)

    # Imprima os valores na tabela
    print(f"{valor:.2f}     | {quadrado:.2f}     | {cubo:.2f}     | {raiz_quadrada:.2f}")
    
    # Atualize o contador de linhas
    linha_count += 1

print("Fim do programa.")
