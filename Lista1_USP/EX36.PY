#X36: Faça um programa que receba a idade e a altura de várias pessoas e que calcule e mostre a média das alturas das pessoas com mais de 50 anos. Para encerrar a entrada de dados digite idade menor ou igual a zero.

# Inicializando as variáveis
soma_alturas = 0
contador = 0

# Coletando as idades e as alturas
while True:
    idade = int(input("Digite a idade (ou um valor menor ou igual a zero para sair): "))
    if idade <= 0:
        break
    altura = float(input("Digite a altura: "))

    if idade > 50:
        soma_alturas += altura
        contador += 1

# Calculando a média das alturas
media_alturas = soma_alturas / contador if contador > 0 else 0

# Mostrando a média das alturas
print("Média das alturas das pessoas com mais de 50 anos:", media_alturas)
