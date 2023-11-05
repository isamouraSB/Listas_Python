#EX30: Uma empresa deseja aumentar seus preços em 20%. Faça um programa que leia o código e o preço de custo de cada produto e que calcule o novo preço. Calcule também a média dos preços com e sem aumento. Mostre o código e o novo preço de cada produto e no final, as médias. A entrada de dados deve terminar quando for lido um código de produ- to negativo.

# Inicializando as variáveis
soma_precos_sem_aumento = 0
soma_precos_com_aumento = 0
contador = 0

# Coletando os dados
while True:
    codigo = int(input("Digite o código do produto (ou um valor negativo para sair): "))
    if codigo < 0:
        break
    preco_custo = float(input("Digite o preço de custo do produto: "))

    # Calculando o novo preço
    novo_preco = preco_custo * 1.2

    soma_precos_sem_aumento += preco_custo
    soma_precos_com_aumento += novo_preco
    contador += 1

    # Mostrando o código e o novo preço do produto
    print("Código do produto:", codigo)
    print("Novo preço do produto:", novo_preco)

# Calculando as médias dos preços com e sem aumento
media_precos_sem_aumento = soma_precos_sem_aumento / contador if contador > 0 else 0
media_precos_com_aumento = soma_precos_com_aumento / contador if contador > 0 else 0

# Mostrando as médias dos preços com e sem aumento
print("Média dos preços sem aumento:", media_precos_sem_aumento)
print("Média dos preços com aumento:", media_precos_com_aumento)
