#EX19: Faça um programa que receba várias idades e que calcule e mostre a média das idades digitadas. Finalize digitando a idade igual a zero.

# Inicializando as variáveis
soma_idades = 0
contador = 0

# Coletando as idades
while True:
    idade = int(input("Digite uma idade (ou 0 para sair): "))
    if idade == 0:
        break
    soma_idades += idade
    contador += 1

# Calculando a média das idades
media_idades = soma_idades / contador if contador > 0 else 0

# Mostrando a média das idades
print("Média das idades:", media_idades)
