#EX12:  Faça um programa que receba a idade, a altura e o peso de 25 pessoas. Calcule e mostre:
#•	a quantidade de pessoas com idade superior a 50 anos: 
#•	a média das alturas das pessoas com idade entre 10 e 20 anos;
#•	a percentagem de pessoas com peso inferior a 40 quilos entre todas as pessoas
#•	analisadas.

# Inicialize variáveis para armazenar os resultados
pessoas_acima_de_50 = 0
altura_total = 0
altura_pessoas_entre_10_e_20 = 0
peso_total = 0
pessoas_com_peso_abaixo_de_40 = 0

# Loop para coletar dados de 25 pessoas
for i in range(1, 26):
    print(f"Informações da pessoa {i}:")
    idade = int(input("Idade: "))
    altura = float(input("Altura (em metros): "))
    peso = float(input("Peso (em quilos): "))
    
    # Verifica idade acima de 50 anos
    if idade > 50:
        pessoas_acima_de_50 += 1
    
    # Verifica altura das pessoas entre 10 e 20 anos
    if idade >= 10 and idade <= 20:
        altura_pessoas_entre_10_e_20 += altura
    
    # Verifica peso abaixo de 40 quilos
    if peso < 40:
        pessoas_com_peso_abaixo_de_40 += 1
    
    # Atualiza a soma das alturas e pesos
    altura_total += altura
    peso_total += peso

# Calcula a média das alturas das pessoas entre 10 e 20 anos
media_altura_entre_10_e_20 = altura_pessoas_entre_10_e_20 / 25

# Calcula a porcentagem de pessoas com peso inferior a 40 quilos
porcentagem_peso_abaixo_de_40 = (pessoas_com_peso_abaixo_de_40 / 25) * 100

# Exibe os resultados
print(f"Quantidade de pessoas com idade superior a 50 anos: {pessoas_acima_de_50}")
print(f"Média das alturas das pessoas entre 10 e 20 anos: {media_altura_entre_10_e_20:.2f} metros")
print(f"Percentagem de pessoas com peso inferior a 40 quilos: {porcentagem_peso_abaixo_de_40:.2f}%")



