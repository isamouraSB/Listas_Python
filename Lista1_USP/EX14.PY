#EX14: Faça um programa que receba a idade, o peso, a altura a cor dos olhos (A-Azul, P-Preto, V-Verde e C-Castanho) e a cor dos cabelos (P-Preto, C-Castanho, L-Louro e R-Ruivo) de 20 pessoas e que calcule e mostre:
#•	a quantidade de pessoas com idade superior a 50 anos e peso inferior a 60 quilos;
#•	a média das idades das pessoas com altura inferior a 1.50;
#•	a percentagem de pessoas com olhos azuis entre todas as pessoas analisadas;
#•	a quantidade de pessoas ruivas e que não possuem olhos azuis;

# Inicializando as variáveis
pessoas_idade_50_peso_60 = 0
soma_idades_altura_150 = 0
contador_altura_150 = 0
pessoas_olhos_azuis = 0
pessoas_ruivas_olhos_nao_azuis = 0

# Coletando os dados de 20 pessoas
for i in range(20):
    idade = int(input("Digite a idade: "))
    peso = float(input("Digite o peso: "))
    altura = float(input("Digite a altura: "))
    cor_olhos = input("Digite a cor dos olhos (A-Azul, P-Preto, V-Verde, C-Castanho): ")
    cor_cabelos = input("Digite a cor dos cabelos (P-Preto, C-Castanho, L-Louro, R-Ruivo): ")

    if idade > 50 and peso < 60:
        pessoas_idade_50_peso_60 += 1

    if altura < 1.50:
        soma_idades_altura_150 += idade
        contador_altura_150 += 1

    if cor_olhos == 'A':
        pessoas_olhos_azuis += 1

    if cor_cabelos == 'R' and cor_olhos != 'A':
        pessoas_ruivas_olhos_nao_azuis += 1

# Calculando a média das idades das pessoas com altura inferior a 1.50
media_idades_altura_150 = soma_idades_altura_150 / contador_altura_150 if contador_altura_150 > 0 else 0

# Calculando a percentagem de pessoas com olhos azuis
percentagem_olhos_azuis = (pessoas_olhos_azuis / 20) * 100

# Mostrando os resultados
print("Quantidade de pessoas com idade superior a 50 anos e peso inferior a 60 quilos:", pessoas_idade_50_peso_60)
print("Média das idades das pessoas com altura inferior a 1.50:", media_idades_altura_150)
print("Percentagem de pessoas com olhos azuis:", percentagem_olhos_azuis)
print("Quantidade de pessoas ruivas e que não possuem olhos azuis:", pessoas_ruivas_olhos_nao_azuis)
