#EX11: Uma loja utiliza o código V para transação à vista e P para transação a prazo. Faça um programa que receba o código e o valor de 15 transações. Calcule e mostre:
#•	valor total das compras à vista:
#•	o valor total das compras a prazo,
#•	o valor total das compras efetuadas;
#•	o valor da primeira prestação das compras a prazo, sabendo-se que essas serão pagas em três vezes.

# total
total_vista = 0
total_prazo = 0


for i in range(15):
    codigo = input("Digite o código da transação (V para à vista, P para a prazo): ")
    valor = float(input("Digite o valor da transação: "))
    
    if codigo.upper() == "V":
        total_vista += valor
    elif codigo.upper() == "P":
        total_prazo += valor

total_compras = total_vista + total_prazo
primeira_prestacao = total_prazo / 3

print(f"Valor total das compras à vista: R${total_vista}")
print(f"Valor total das compras a prazo: R${total_prazo}")
print(f"Valor total das compras efetuadas: R${total_compras}")
print(f"Valor da primeira prestação das compras a prazo: R${primeira_prestacao}")
