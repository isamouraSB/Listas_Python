#EX16.: Faça um programa que receba de idades, pesos e alturas e que calcule e mostre:
#•	A média das idades das dez pessoas;
#•	a quantidade de pessoas com pese superior 90 quilos e altura inferior a 1,50;
#•	a percentagens de pessoas com idade entre 10 e 30 anos entre as pessoas que medem mais de 1.90;

# Inicializando as variáveis
soma_idades = 0
pessoas_peso_90_altura_150 = 0
pessoas_idade_10_30_altura_190 = 0
pessoas_altura_190 = 0

# Coletando os dados de 10 pessoas
for i in range(10):
    idade = int(input("Digite a idade: "))
    peso = float(input("Digite o peso: "))
    altura = float(input("Digite a altura: "))

    soma_idades += idade

    if peso > 90 and altura < 1.50:
        pessoas_peso_90_altura_150 += 1

    if altura > 1.90:
        pessoas_altura_190 += 1
        if 10 < idade < 30:
            pessoas_idade_10_30_altura_190 += 1

# Calculando a média das idades
media_idades = soma_idades / 10

# Calculando a percentagem de pessoas com idade entre 10 e 30 anos entre as pessoas que medem mais de 1.90
percentagem_idade_10_30_altura_190 = (pessoas_idade_10_30_altura_190 / pessoas_altura_190) * 100 if pessoas_altura_190 > 0 else 0

# Mostrando os resultados
print("Média das idades das dez pessoas:", media_idades)
print("Quantidade de pessoas com peso superior a 90 quilos e altura inferior a 1.50:", pessoas_peso_90_altura_150)
print("Percentagem de pessoas com idade entre 10 e 30 anos entre as pessoas que medem mais de 1.90:", percentagem_idade_10_30_altura_190)
