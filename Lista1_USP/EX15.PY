#EX15: Faça um programa que receba dez números e que calcule e mostre a quantidade de números entre 30 e 90

# Inicializando a variável
quantidade_numeros = 0

# Coletando os dados de 10 números
for i in range(10):
    numero = float(input("Digite um número: "))

    if 30 < numero < 90:
        quantidade_numeros += 1

# Mostrando o resultado
print("Quantidade de números entre 30 e 90:", quantidade_numeros)
