#EX23: Cada espectador de um cinema respondeu a um questionário no qual constava sua idade e a sua opinião em relação ao filme: ótimo - 3, bom - 2, regular - 1. Faça um programa que receba a idade e a opinião de 15 espectadores e que calcule e mostre:
#•	A média das idades das pessoas que responderam ótimo:
#•	A quantidade de pessoas que respondeu regular:
#•	A percentagem de pessoas que respondeu bom entre todos os espectadores analisados.

# Inicializando as variáveis
soma_idades_otimo = 0
contador_otimo = 0
contador_regular = 0
contador_bom = 0

# Coletando os dados de 15 espectadores
for i in range(15):
    idade = int(input("Digite a idade: "))
    opiniao = int(input("Digite a opinião (3 - ótimo, 2 - bom, 1 - regular): "))

    if opiniao == 3:
        soma_idades_otimo += idade
        contador_otimo += 1
    elif opiniao == 2:
        contador_bom += 1
    elif opiniao == 1:
        contador_regular += 1

# Calculando a média das idades das pessoas que responderam ótimo
media_idades_otimo = soma_idades_otimo / contador_otimo if contador_otimo > 0 else 0

# Calculando a percentagem de pessoas que respondeu bom
percentagem_bom = (contador_bom / 15) * 100

# Mostrando os resultados
print("Média das idades das pessoas que responderam ótimo:", media_idades_otimo)
print("Quantidade de pessoas que respondeu regular:", contador_regular)
print("Percentagem de pessoas que respondeu bom:", percentagem_bom)
