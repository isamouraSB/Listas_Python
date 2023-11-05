#EX7: Faça um programa que receba a idade de dez pessoas e que calcule e mostre a quantidade de pessoas com idade maior ou igual a 18 anos. 

# Inicialize uma variável para contar a quantidade de pessoas com 18 anos ou mais
quantidade_maiores_dezoito = 0

# Faça um loop para receber a idade de dez pessoas
for i in range(10):
    idade = int(input(f"Digite a idade da pessoa {i + 1}: "))

    # Verifique se a idade é maior ou igual a 18
    if idade >= 18:
        quantidade_maiores_dezoito += 1

# Exiba a quantidade de pessoas com idade maior ou igual a 18 anos
print(f"Quantidade de pessoas com 18 anos ou mais: {quantidade_maiores_dezoito}")
