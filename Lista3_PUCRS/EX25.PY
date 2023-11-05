#EX25: Uma empresa deseja aumentar seus preços em 20%. Faça um algoritmo que leia o código e o preço de custo de cada produto e calcule o preço novo. Calcule também, a média dos preços com e sem aumento. Mostre o código e o preço novo de cada produto e, no final, as médias. A entrada de dados deve terminar quando for lido um código de produto negativo. (Use o comando enquanto-faça)

soma_precos_com_aumento = 0
soma_precos_sem_aumento = 0
contagem_produtos = 0

while True:
    codigo = int(input("Digite o código do produto (negativo para sair): "))

    if codigo < 0:
        break

    preco_custo = float(input("Digite o preço de custo: "))
    novo_preco = preco_custo * 1.20  # Aumento de 20%

    soma_precos_com_aumento += novo_preco
    soma_precos_sem_aumento += preco_custo
    contagem_produtos += 1

    print(f"Código do produto: {codigo}, Preço novo: {novo_preco:.2f}")

if contagem_produtos > 0:
    media_preco_com_aumento = soma_precos_com_aumento / contagem_produtos
    media_preco_sem_aumento = soma_precos_sem_aumento / contagem_produtos
else:
    media_preco_com_aumento = 0
    media_preco_sem_aumento = 0

print(f"Média dos preços com aumento: {media_preco_com_aumento:.2f}")
print(f"Média dos preços sem aumento: {media_preco_sem_aumento:.2f}")
