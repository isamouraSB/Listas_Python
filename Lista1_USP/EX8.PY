#EX8: Faça um programa que receba a idade de 15 pessoas e que calcule e mostre: 
# a quantidade de pessoas em cada faixa etária;
# a porcentagem de pessoas na primeira e na última faixa etária, com relação ao total de pessoas. 

# # Inicialize uma variável para contar a  quantidade da idade das pessoas
quantidade_1 = 0 # até 15
quantidade_2 = 0 # 16 a 30
quantidade_3 = 0 # 31 a 45
quantidade_4 = 0 # 46 a 60
quantidade_5 = 0 # acima 61

# Número total de pessoas
total_pessoas = 15

# Faça um loop para receber a idade de dez pessoas
for i in range(total_pessoas):
    idade = int(input(f"Digite a idade da pessoa {i + 1}: "))

    # Verifique a idade
    if idade <= 15:
        quantidade_1 += 1
    elif 16 <= idade <= 30:
        quantidade_2 += 1 
    elif 31 <= idade <= 45:
        quantidade_3 += 1
    elif 46 <= idade <= 60:
        quantidade_4 += 1
    elif idade >= 61:
        quantidade_5 += 1
    
# Cálculo das percentagens
percentagem_primeira_faixa = (quantidade_1 / total_pessoas) * 100
percentagem_ultima_faixa = (quantidade_5 / total_pessoas) * 100

       
# Exiba a quantidade de pessoas com idade maior ou igual a 18 anos
print(f"Quantidade de pessoas até 15 anos: {quantidade_1}")
print(f"Quantidade de pessoas de 16 a 31: {quantidade_2}")
print(f"Quantidade de pessoas de 31 a 45: {quantidade_3}")
print(f"Quantidade de pessoas de 46 a 60: {quantidade_4}")
print(f"Quantidade de pessoas acima de 61 anos: {quantidade_5}")

# Exibir as percentagens da primeira e última faixa etária
print(f"Percentagem de pessoas na primeira faixa etária: {percentagem_primeira_faixa:.2f}%")
print(f"Percentagem de pessoas na última faixa etária: {percentagem_ultima_faixa:.2f}%")