# EX2:Faça um programa que leia um valor n, inteiro e positivo, calcule e mostre a seguinte soma: 
#S= 1 + ½ + 1/3 + ¼ + ... 1/n 

n = int(input("Digite um número inteiro e positivo: ")) 
def calcular_soma(n):
    S = 0
    for i in range(1, n+1):
        S += 1/i
        return S

print("O resultado é:", calcular_soma(n))
