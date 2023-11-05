#EX22: Faça um programa que receba a idade e o peso de 15 pessoas. Calcule e mostre as médias dos pesos das pessoas da mesma faixa etária. As faixas etárias são: de 1 a 10 anos, de 11 a 20 anos, de 21 a 30 anos e maiores de 31 anos.

# Inicializando as variáveis
soma_pesos_1_10 = 0
contador_1_10 = 0
soma_pesos_11_20 = 0
contador_11_20 = 0
soma_pesos_21_30 = 0
contador_21_30 = 0
soma_pesos_31 = 0
contador_31 = 0

# Coletando os dados de 15 pessoas
for i in range(15):
    idade = int(input("Digite a idade: "))
    peso = float(input("Digite o peso: "))

    if 1 <= idade <= 10:
        soma_pesos_1_10 += peso
        contador_1_10 += 1
    elif 11 <= idade <= 20:
        soma_pesos_11_20 += peso
        contador_11_20 += 1
    elif 21 <= idade <= 30:
        soma_pesos_21_30 += peso
        contador_21_30 += 1
    elif idade > 31:
        soma_pesos_31 += peso
        contador_31 += 1

# Calculando as médias dos pesos
media_pesos_1_10 = soma_pesos_1_10 / contador_1_10 if contador_1_10 > 0 else 0
media_pesos_11_20 = soma_pesos_11_20 / contador_11_20 if contador_11_20 > 0 else 0
media_pesos_21_30 = soma_pesos_21_30 / contador_21_30 if contador_21_30 > 0 else 0
media_pesos_31 = soma_pesos_31 / contador_31 if contador_31 > 0 else 0

# Mostrando as médias dos pesos
print("Média dos pesos das pessoas de 1 a 10 anos:", media_pesos_1_10)
print("Média dos pesos das pessoas de 11 a 20 anos:", media_pesos_11_20)
print("Média dos pesos das pessoas de 21 a 30 anos:", media_pesos_21_30)
print("Média dos pesos das pessoas maiores de 31 anos:", media_pesos_31)
