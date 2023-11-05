#EX5: Uma loja tem 15 clientes cadastrados e deseja enviar uma correspondência a cada um deles anunciando um bônus especial. Faça um programa que leias o nome do cliente e o valor de suas compras no ano passado. Calcule e mostre um bônus de 10% se o valor das compras for menor que R$ 1.000,00 e de 15%, caso contrário.

# Função para ler os dados do cliente
def ler_dados_cliente():
    clientes = []
    for i in range(15):
        nome = input("Insira o nome do cliente: ")
        valor_compras = float(input("Insira o valor das compras do ano passado: "))
        clientes.append((nome, valor_compras))
    return clientes

# Função para calcular e mostrar o bônus
def calcular_bonus(clientes):
    for nome, valor_compras in clientes:
        if valor_compras < 1000:
            bonus = valor_compras * 0.10
        else:
            bonus = valor_compras * 0.15
        print(f"O cliente {nome} tem um bônus de R$ {bonus:.2f}")

# Programa principal
def main():
    clientes = ler_dados_cliente()
    calcular_bonus(clientes)

# Executar o programa principal
if __name__ == "__main__":
    main()
