#EX39: Uma agência bancária possui vários clientes que podem fazer investimentos com rendimentos mensais, conforme a tabela a seguir:
#tipo	descrição	Rendimento mensal
#1	poupança	1,5 %
#2	Poupança plus	2 %
#3	Fundos de renda fixa	4 % 
#Faça um programa que leia o código do cliente, o tipo da conta e o valor investido e que calcule e mostre o rendimento mensal de acordo com o tipo do investimento. Ao final do programa mostre o total investido e o total de juros pagos.
#A leitura terminará quando o código do cliente digitado for menor ou igual a 0.

total_investido = 0
total_juros = 0

while True:
    codigo_cliente = int(input("Informe o código do cliente (0 para sair): "))
    if codigo_cliente <= 0:
        break

    tipo_conta = int(input("Informe o tipo da conta (1 - poupança, 2 - Poupança plus, 3 - Fundos de renda fixa): "))
    valor_investido = float(input("Informe o valor investido: "))

    if tipo_conta == 1:
        rendimento = valor_investido * 0.015
    elif tipo_conta == 2:
        rendimento = valor_investido * 0.02
    elif tipo_conta == 3:
        rendimento = valor_investido * 0.04
    else:
        print("Tipo de conta inválido.")
        continue

    print(f"O rendimento mensal é R$ {rendimento:.2f}")

    total_investido += valor_investido
    total_juros += rendimento

print(f"Total investido: R$ {total_investido:.2f}")
print(f"Total de juros pagos: R$ {total_juros:.2f}")
