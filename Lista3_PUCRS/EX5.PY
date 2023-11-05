#EX5: Construir um algoritmo que calcule a média aritmética de vários valores inteiros positivos, lidos externamente. O final da leitura acontecerá quando for lido um valor negativo.

# Inicialize as variáveis
soma = 0
contagem = 0
valor = int(input("Insira um valor inteiro positivo (ou um valor negativo para sair): "))

# Faça um loop para ler os valores até que um valor negativo seja inserido
while True:
    if valor < 0:
        break  # Saia do loop se um valor negativo for inserido
    
    soma += valor
    contagem += 1

# Certifique-se de que pelo menos um valor positivo tenha sido inserido para evitar divisão por zero
if contagem > 0:
    media = soma / contagem
    print(f"A média dos valores inseridos é: {media}")
else:
    print("Nenhum valor positivo foi inserido.")

