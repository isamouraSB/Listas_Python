#EX44: Foi feita uma estatística nas 200 principais cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:
#- código da cidade
#- estado (RS, SC, PR, SP, RJ, ...)
#- número de veículos de passeio (em 1992)
#- número de acidentes de trânsito com vítimas (em 1992)
#Deseja-se saber:
#a) qual o maior e o menor índice de acidentes de trânsito e a que cidades pertencem
#b) qual a média de veículos nas cidades brasileiras
#c) qual a média de acidentes com vítimas entre as cidades do Rio Grande do Sul

# Variáveis para acompanhar o maior e o menor índice de acidentes
maior_indice = float('-inf')
cidade_maior_indice = ""
menor_indice = float('inf')
cidade_menor_indice = ""

# Variáveis para calcular a média de veículos e acidentes com vítimas no RS
soma_veiculos_RS = 0
soma_acidentes_vitimas_RS = 0
contagem_cidades_RS = 0

# Ler dados de 200 cidades
for cidade in range(1, 201):
    codigo = int(input("Código da cidade: "))
    estado = input("Estado (RS, SC, PR, SP, RJ, ...): ")
    veiculos = int(input("Número de veículos de passeio (em 1992): "))
    acidentes = int(input("Número de acidentes de trânsito com vítimas (em 1992): "))

    # Verifique o maior e o menor índice de acidentes
    indice = acidentes / veiculos
    if indice > maior_indice:
        maior_indice = indice
        cidade_maior_indice = codigo
    if indice < menor_indice:
        menor_indice = indice
        cidade_menor_indice = codigo

    # Calcule a média de veículos para todas as cidades
    soma_veiculos += veiculos

    # Verifique se a cidade está no Rio Grande do Sul
    if estado == "RS":
        soma_veiculos_RS += veiculos
        soma_acidentes_vitimas_RS += acidentes
        contagem_cidades_RS += 1

# Calcular a média de veículos para todas as cidades
media_veiculos = soma_veiculos / 200

# Calcular a média de acidentes com vítimas entre as cidades do Rio Grande do Sul
if contagem_cidades_RS > 0:
    media_acidentes_vitimas_RS = soma_acidentes_vitimas_RS / contagem_cidades_RS
else:
    media_acidentes_vitimas_RS = 0

# Imprimir os resultados
print(f"Maior índice de acidentes: {maior_indice} na cidade {cidade_maior_indice}")
print(f"Menor índice de acidentes: {menor_indice} na cidade {cidade_menor_indice}")
print(f"Média de veículos nas cidades brasileiras: {media_veiculos:.2f}")
print(f"Média de acidentes com vítimas no Rio Grande do Sul: {media_acidentes_vitimas_RS:.2f}")
