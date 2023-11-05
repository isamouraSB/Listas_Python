#EX12: Construa um programa que leia dois números inteiros a e b, uma lista de
#tamanho N e exiba como resposta a contagem de quantos elementos do
#vetor estão no intervalo fechado [a; b].

# Ler os números inteiros a e b
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))

# Ler o tamanho da lista N
N = int(input("Digite o tamanho da lista: "))

# Inicializar uma lista vazia para armazenar os elementos
lista = []

# Ler os elementos da lista
for i in range(N):
    elemento = int(input(f"Digite o {i+1}º elemento: "))
    lista.append(elemento)

# Inicializar uma variável para contar quantos elementos estão no intervalo [a; b]
contagem = 0

# Contar quantos elementos estão no intervalo [a; b]
for elemento in lista:
    if a <= elemento <= b:
        contagem += 1

# Exibir o resultado
print(f"A contagem de elementos no intervalo [{a}; {b}] é: {contagem}")
