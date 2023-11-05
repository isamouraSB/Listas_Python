#EX28: A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados sobre o salário e o número de filhos. A prefeitura deseja saber:
#a) a média do salário da população;
#b) a média do número de filhos;
#c) o maior salário:
#d) a percentagem de pessoas com salários até R$ 150,00.
#O final da leitura de dados dar-se-á com a entrada de um salário negativo.

# Inicializando as variáveis
soma_salarios = 0
soma_filhos = 0
contador = 0
maior_salario = -1
salarios_ate_150 = 0

# Coletando os dados
while True:
    salario = float(input("Digite o salário (ou um valor negativo para sair): "))
    if salario < 0:
        break
    filhos = int(input("Digite o número de filhos: "))

    soma_salarios += salario
    soma_filhos += filhos
    contador += 1

    if salario > maior_salario:
        maior_salario = salario

    if salario <= 150:
        salarios_ate_150 += 1

# Calculando as médias e a percentagem
media_salarios = soma_salarios / contador if contador > 0 else 0
media_filhos = soma_filhos / contador if contador > 0 else 0
percentagem_salarios_ate_150 = (salarios_ate_150 / contador) * 100 if contador > 0 else 0

# Mostrando os resultados
print("Média do salário da população:", media_salarios)
print("Média do número de filhos:", media_filhos)
print("Maior salário:", maior_salario)
print("Percentagem de pessoas com salários até R$ 150,00:", percentagem_salarios_ate_150)

