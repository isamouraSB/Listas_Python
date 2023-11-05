#EX45: Foi feita uma pesquisa entre os 1000 habitantes de uma região para coletar os seguintes dados: sexo (0-feminino, 1-masculino), idade e altura. Faça um algoritmo que leia as informações coletadas e mostre as seguintes informações: (use o comando repita-até)
#a) média da idade do grupo;
#b) média da altura das mulheres;
#c) média da idade dos homens;
#d) percentual de pessoas com idade entre 18 e 35 anos (inclusive)

# Inicialize as variáveis
soma_idade = 0
soma_altura_mulheres = 0
soma_idade_homens = 0
contagem_mulheres = 0
contagem_homens = 0
contagem_jovens = 0

# Loop para ler as informações de 1000 habitantes
contador = 0
while contador < 1000:
    sexo = int(input("Digite o sexo (0-feminino, 1-masculino): "))
    idade = int(input("Digite a idade: "))
    altura = float(input("Digite a altura: "))

    # Calcula a média da idade do grupo
    soma_idade += idade

    # Calcula a média da altura das mulheres
    if sexo == 0:
        soma_altura_mulheres += altura
        contagem_mulheres += 1

    # Calcula a média da idade dos homens
    if sexo == 1:
        soma_idade_homens += idade
        contagem_homens += 1

    # Calcula o percentual de pessoas com idade entre 18 e 35 anos
    if 18 <= idade <= 35:
        contagem_jovens += 1

    contador += 1

# Calcula as médias
media_idade_grupo = soma_idade / 1000

if contagem_mulheres > 0:
    media_altura_mulheres = soma_altura_mulheres / contagem_mulheres
else:
    media_altura_mulheres = 0

if contagem_homens > 0:
    media_idade_homens = soma_idade_homens / contagem_homens
else:
    media_idade_homens = 0

percentual_jovens = (contagem_jovens / 1000) * 100

# Imprime as informações
print(f"Média da idade do grupo: {media_idade_grupo:.2f}")
print(f"Média da altura das mulheres: {media_altura_mulheres:.2f}")
print(f"Média da idade dos homens: {media_idade_homens:.2f}")
print(f"Percentual de pessoas com idade entre 18 e 35 anos: {percentual_jovens:.2f}%")
