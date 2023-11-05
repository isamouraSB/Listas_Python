#EX12; Escrever um algoritmo que leia 20 valores para uma variável n e, para cada um deles, calcule a tabuada de 1 até n. Mostre a tabuada na forma:
#1 x n = n
#2 x n = 2n
#3 x n = 3n
#.......
#n x n = n2

for _ in range(20):
    n = int(input("Digite um valor para n: "))
    for i in range(1, n+1):
        print(f"{i} x {n} = {i*n}")
