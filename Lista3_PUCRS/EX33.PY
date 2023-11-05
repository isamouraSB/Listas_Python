#EX33: Escrever um algoritmo que leia 20 valores para uma variável N e, para cada um deles, calcule a tabuada de 1 até N. Mostre a tabuada na forma: 1 x N = N 2 x N = 2N 3 x
# N = 3N ...... N x N = N2 

for _ in range(20):
    N = int(input("Digite um valor para N: "))
    for i in range(1, N + 1):
        print(f"{i} x {N} = {i * N}")
