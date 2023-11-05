#EX27: Escreva um algoritmo que leia 500 valores inteiros e positivos e:
#a) encontre o maior valor;
#b) encontre o menor valor;
#c) calcule a média dos números lidos.

maior_valor = float('-inf')
menor_valor = float('inf')
soma_valores = 0

for _ in range(500):
    valor = int(input("Digite um valor inteiro e positivo: "))

    if valor > maior_valor:
        maior_valor = valor

    if valor < menor_valor:
        menor_valor = valor

    soma_valores += valor

media_valores = soma_valores / 500

print(f"Maior valor: {maior_valor}")
print(f"Menor valor: {menor_valor}")
print(f"Média dos valores: {media_valores}")
