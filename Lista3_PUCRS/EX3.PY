#EX3: A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados sobre o salário e número de filhos. A prefeitura deseja saber:
#a) média do salário da população;
#b) média do número de filhos;
#c) maior salário;
#d) percentual de pessoas com salário até R$100,00.
#O final da leitura de dados se dará com a entrada de um salário negativo. (Use o comando ENQUANTO-FAÇA)

# Inicialize as variáveis
total_salario = 0
total_filhos = 0
maior_salario = float('-inf')  # Inicialize com um valor negativo para garantir que o primeiro salário seja maior
pessoas_com_salario_ate_100 = 0

# Loop para ler os dados dos habitantes
while True:
    salario = float(input("Digite o salário do habitante (ou um valor negativo para encerrar): "))
    
    if salario < 0:
        break
    
    numero_de_filhos = int(input("Digite o número de filhos: "))
    
    total_salario += salario
    total_filhos += numero_de_filhos
    
    if salario > maior_salario:
        maior_salario = salario
    
    if salario <= 100:
        pessoas_com_salario_ate_100 += 1

# Calcule as médias
media_salario = total_salario / (pessoas_com_salario_ate_100 + 1)  # Adicionamos 1 para incluir o último habitante
media_filhos = total_filhos / (pessoas_com_salario_ate_100 + 1)

# Calcule o percentual de pessoas com salário até R$100,00
percentual_salario_ate_100 = (pessoas_com_salario_ate_100 / (pessoas_com_salario_ate_100 + 1)) * 100

# Exiba os resultados
print(f"Média do salário da população: R${media_salario:.2f}")
print(f"Média do número de filhos: {media_filhos:.2f}")
print(f"Maior salário: R${maior_salario:.2f}")
print(f"Percentual de pessoas com salário até R$100,00: {percentual_salario_ate_100:.2f}%")
