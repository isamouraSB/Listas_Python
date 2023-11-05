#EX5:Escreva um programa que leia três vetores do mesmo tamanho (N) e:
#a) calcule a norma de cada um dos vetores, informe qual vetor tem a maior norma1 ;
#b) calcule o vetor soma dos três vetores2.

import math

def calcular_norma(vetor):
    norma = math.sqrt(sum([x ** 2 for x in vetor]))
    return norma

def calcular_vetor_soma(vetor1, vetor2, vetor3):
    vetor_soma = [x + y + z for x, y, z in zip(vetor1, vetor2, vetor3)]
    return vetor_soma

# Tamanho dos vetores (N)
N = int(input("Digite o tamanho dos vetores: "))

# Inicialização dos vetores
vetor1 = []
vetor2 = []
vetor3 = []

# Leitura dos valores dos vetores
print("Digite os valores do primeiro vetor:")
for _ in range(N):
    valor = float(input())
    vetor1.append(valor)

print("Digite os valores do segundo vetor:")
for _ in range(N):
    valor = float(input())
    vetor2.append(valor)

print("Digite os valores do terceiro vetor:")
for _ in range(N):
    valor = float(input())
    vetor3.append(valor)

# Calcula a norma de cada vetor
norma_vetor1 = calcular_norma(vetor1)
norma_vetor2 = calcular_norma(vetor2)
norma_vetor3 = calcular_norma(vetor3)

# Encontra o vetor com a maior norma
maior_norma = max(norma_vetor1, norma_vetor2, norma_vetor3)
if maior_norma == norma_vetor1:
    vetor_com_maior_norma = vetor1
elif maior_norma == norma_vetor2:
    vetor_com_maior_norma = vetor2
else:
    vetor_com_maior_norma = vetor3

print(f"O vetor com a maior norma é {vetor_com_maior_norma} com norma {maior_norma:.2f}")

# Calcula o vetor soma
vetor_soma = calcular_vetor_soma(vetor1, vetor2, vetor3)
print("Vetor Soma: ", vetor_soma)
