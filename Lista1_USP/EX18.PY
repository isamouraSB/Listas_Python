#EX18: Faça um programa que receba o valor de um carro e mostre uma tabela com os seguintes dados: preço final, quantidade de parcelas e valor da parcela. Considere o seguinte:
#1. O preço final para compra à vista tem um desconto de 20%.
#2. A quantidade de parcelas pode ser: 6, 12, 18, 24, 30, 36, 42, 48, 54 e 60.
#3. Os percentuais de acréscimo seguem a tabela a seguir.
 
 # Recebendo o valor do carro
valor_carro = float(input("Digite o valor do carro: "))

# Calculando o preço final para compra à vista
preco_final_vista = valor_carro * 0.8

print("Preço final à vista: R$", preco_final_vista)

# Definindo as parcelas e os percentuais de acréscimo
parcelas = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60]
acrescimos = [0.03, 0.06, 0.09, 0.12, 0.15, 0.18, 0.21, 0.24, 0.27, 0.30]

# Calculando o preço final, a quantidade de parcelas e o valor da parcela
for i in range(len(parcelas)):
    preco_final = valor_carro * (1 + acrescimos[i])
    valor_parcela = preco_final / parcelas[i]
    print("Preço final para", parcelas[i], "parcelas: R$", preco_final)
    print("Valor da parcela: R$", valor_parcela)
