#EX29: Escrever um algoritmo que calcule e mostre a média aritmética dos números lidos entre 13 e 73.

# Inicialize as variáveis
soma = 0
contagem = 0

# Faça um loop para ler os valores e calcular a soma
while True:
    valor = int(input("Digite um número (ou -1 para sair): "))
    
    if valor == -1:
        break
    
    if 13 <= valor <= 73:
        soma += valor
        contagem += 1

# Verifique se pelo menos um valor foi lido para evitar a divisão por zero
if contagem > 0:
    media = soma / contagem
    print(f"A média dos números entre 13 e 73 é: {media:.2f}")
else:
    print("Nenhum número entre 13 e 73 foi inserido.")
