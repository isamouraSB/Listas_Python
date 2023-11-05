#EX6: Uma companhia de teatro deseja dar uma serie de espetáculos. A direção calcula que a R$ 5,00 o ingresso, serão vendidos 120 ingressos, e que as despesas serão R$ 200,00. Diminuindo-se R$ 0,50 o preço dos ingressos espera-se que as vendas aumentem em 26 ingressos. Faça um programa que escreva uma tabela de valores de lucros esperados em função do preço do ingresso, fazendo-se variar esse preço de R$ 5,00 a r$ 1,00 de R$ 0,50 EM r$ 0,50. Escreva, ainda, o lucro máximo esperado, o preço do ingresso e a quantidade de ingressos vendidos para a obtenção desse lucro.

# Preço inicial do ingresso, despesas e quantidade inicial de ingressos vendidos
preco_ingresso = 5.00
despesas = 200.00
quantidade_inicial = 120

# Variáveis para armazenar o lucro máximo esperado e suas informações
lucro_maximo = 0
preco_maximo = 0
quantidade_maxima = 0

# Loop para variar o preço do ingresso de R$ 5,00 a R$ 1,00, com intervalo de R$ 0,50
for novo_preco_ingresso in range(500, 0, -50):
    novo_preco_ingresso /= 100  # Converter de centavos para reais
    quantidade_vendida = quantidade_inicial + 26  # Aumento de 26 ingressos nas vendas

    # Cálculo da receita, lucro e lucro máximo esperado
    receita = novo_preco_ingresso * quantidade_vendida
    lucro = receita - despesas

    # Verificar se o lucro atual é maior que o máximo anterior
    if lucro > lucro_maximo:
        lucro_maximo = lucro
        preco_maximo = novo_preco_ingresso
        quantidade_maxima = quantidade_vendida

    # Exibição do preço, quantidade vendida e lucro atual
    print(f"Preço do ingresso: R${novo_preco_ingresso:.2f} | Quantidade Vendida: {quantidade_vendida} | Lucro: R${lucro:.2f}")

# Exibição do lucro máximo esperado, preço do ingresso correspondente e quantidade vendida
print(f"\nLucro Máximo Esperado: R${lucro_maximo:.2f}")
print(f"Preço do Ingresso para Lucro Máximo: R${preco_maximo:.2f}")
print(f"Quantidade de Ingressos Vendidos para Lucro Máximo: {quantidade_maxima}")
