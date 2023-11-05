#EX37: Escrever um algoritmo que leia um valor X e calcule e mostre os 20 primeiros termos da série:
# 1 1 1 1 .....
# X X2 X3 X4

# Lendo o valor de X
X = int(input("Digite um valor para X: "))

# Calculando e mostrando os 20 primeiros termos da série
for i in range(1, 21):
    termo = 1 / (X ** (i - 1))
    print(f"Termo {i}: {termo}")
