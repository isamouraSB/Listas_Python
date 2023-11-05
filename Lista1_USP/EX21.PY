#EX21: Faça um programa para calcular n! (fatorial de n), sendo que o valor inteiro de né fornecido pelo usuário.
#Sabe-se que:
#nt = 1 * 2 * 3 * ... * (n-1) * n;
# 0 = 1, por definição. 

# Recebendo o valor de n
n = int(input("Digite um valor inteiro: "))

# Inicializando o fatorial
fatorial = 1

# Calculando o fatorial de n
for i in range(1, n + 1):
    fatorial *= i

# Mostrando o fatorial de n
print("O fatorial de", n, "é", fatorial)
