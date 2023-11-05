#EX31: Faça um programa que receba o tipo da ação, ou seja, uma letra a ser comercializada na bolsa de valores, o preço de compra e o preço de venda de cada ação e que calcule e mostre:
#•	O lucro de cada ação comercializada;
#•	A quantidade de ações com lucro superior a r$ 1.000,00;
#•	A quantidade de ações com lucro inferior a r$ 200,00;
#•	O lucro total da empresa.
#Finalize com o tipo de ação 'F'.

# Inicializando as variáveis
acoes_lucro_1000 = 0
acoes_lucro_200 = 0
lucro_total = 0

# Coletando os dados
while True:
    tipo_acao = input("Digite o tipo da ação (ou 'F' para sair): ")
    if tipo_acao == 'F':
        break
    preco_compra = float(input("Digite o preço de compra da ação: "))
    preco_venda = float(input("Digite o preço de venda da ação: "))

    # Calculando o lucro da ação
    lucro = preco_venda - preco_compra

    # Atualizando as contagens e o lucro total
    if lucro > 1000:
        acoes_lucro_1000 += 1
    if lucro < 200:
        acoes_lucro_200 += 1
    lucro_total += lucro

    # Mostrando o lucro da ação
    print("Lucro da ação:", lucro)

# Mostrando os resultados
print("Quantidade de ações com lucro superior a R$ 1.000,00:", acoes_lucro_1000)
print("Quantidade de ações com lucro inferior a R$ 200,00:", acoes_lucro_200)
print("Lucro total da empresa:", lucro_total)
