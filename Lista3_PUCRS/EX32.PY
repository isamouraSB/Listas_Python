#EX32: Escrever um algoritmo que lê 5 pares de valores a, b, todos inteiros e positivos, um par de cada vez, e com a < b, escreve os inteiros pares de a até b, incluindo o a e o b se forem pares.

for i in range(5):
    # Lendo os valores de a e b
    a = int(input("Digite o valor de a: "))
    b = int(input("Digite o valor de b (maior que a): "))
    
    # Verificando se a e b são positivos
    if a < 0 or b < 0:
        print("Por favor, digite apenas valores inteiros e positivos.")
        continue
    
    # Verificando se a é menor do que b
    if a >= b:
        print("Por favor, digite um valor de b maior do que a.")
        continue
    
    # Escrevendo os inteiros pares de a até b
    for numero in range(a, b + 1):
        if numero % 2 == 0:
            print(numero)
