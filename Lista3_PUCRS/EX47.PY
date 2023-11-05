#EX47: Uma loja tem 150 clientes cadastrados e deseja mandar uma correspondência a cada um deles anunciando um bônus especial. Escreva um algoritmo que leia o nome do cliente e o valor das suas compras no ano passado e calcule um bônus de 10% se o valor das compras for menor que 500.000 e de15 %, caso contrário.


# Lista para armazenar os dados dos clientes
clientes = []

for _ in range(150):
    # Lendo o nome do cliente e o valor das suas compras no ano passado
    nome = input("Digite o nome do cliente: ")
    valor_compras = float(input("Digite o valor das compras do cliente no ano passado: "))
    
    # Calculando o bônus
    if valor_compras < 500000:
        bonus = valor_compras * 0.10
    else:
        bonus = valor_compras * 0.15
    
    # Adicionando os dados na lista de clientes
    clientes.append((nome, bonus))

# Imprimindo a correspondência para cada cliente
for nome, bonus in clientes:
    print(f"Caro(a) {nome},")
    print(f"Você ganhou um bônus especial de {bonus}!")
    print()
