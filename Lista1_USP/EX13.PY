#EX13: Faça um programa que receba a idade e o peso de sete pessoas. Calcule e mostre:
#•	a quantidade de pessoas com mais de 90 quilos
#•	a média das idades das sete pessoas

# Inicializando as variáveis
total_idade = 0
pessoas_acima_90kg = 0

# Loop para receber a idade e o peso de 7 pessoas
for i in range(1, 8):
    idade = int(input(f"Digite a idade da pessoa {i}: "))
    peso = float(input(f"Digite o peso da pessoa {i} (em kg): "))
    
    # Adicionando a idade ao total
    total_idade += idade
    
    # Verificando se a pessoa pesa mais de 90kg
    if peso > 90:
        pessoas_acima_90kg += 1

# Calculando a média de idade
media_idade = total_idade / 7

# Imprimindo os resultados
print(f"\nQuantidade de pessoas com mais de 90 quilos: {pessoas_acima_90kg}")
print(f"Média das idades: {media_idade}")
