#EX17: Faça um programa que receba a idade e o sexo de sete pessoas e que calcule e mostre:
#•	a idade média do grupo;
#•	a idade média das mulheres;
#•	a idade média dos homens.

# Inicializando as variáveis
soma_idades = 0
soma_idades_mulheres = 0
contador_mulheres = 0
soma_idades_homens = 0
contador_homens = 0

# Coletando os dados de 7 pessoas
for i in range(7):
    idade = int(input("Digite a idade: "))
    sexo = input("Digite o sexo (M para masculino, F para feminino): ")

    soma_idades += idade

    if sexo == 'F':
        soma_idades_mulheres += idade
        contador_mulheres += 1
    elif sexo == 'M':
        soma_idades_homens += idade
        contador_homens += 1

# Calculando a média das idades
media_idades = soma_idades / 7

# Calculando a média das idades das mulheres
media_idades_mulheres = soma_idades_mulheres / contador_mulheres if contador_mulheres > 0 else 0

# Calculando a média das idades dos homens
media_idades_homens = soma_idades_homens / contador_homens if contador_homens > 0 else 0

# Mostrando os resultados
print("Idade média do grupo:", media_idades)
print("Idade média das mulheres:", media_idades_mulheres)
print("Idade média dos homens:", media_idades_homens)

