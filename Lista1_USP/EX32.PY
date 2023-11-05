#EX32: Faça um programa que receba vários números e que calcule e mostre:
#•	A quantidade de números inferiores a 35:
#•	A média dos números positivos:
#•	A percentagem de números entre 50 e 100 entre todos os números digitados;
#•	A percentagem de números entre 10 e 20 entre os números menores que 50.

# Inicializando as variáveis
quantidade_inferior_35 = 0
soma_positivos = 0
contador_positivos = 0
quantidade_50_100 = 0
quantidade_10_20 = 0
quantidade_menor_50 = 0
contador_total = 0

# Coletando os números
while True:
    numero = float(input("Digite um número (ou um valor negativo para sair): "))
    if numero < 0:
        break

    contador_total += 1

    if numero < 35:
        quantidade_inferior_35 += 1

    if numero > 0:
        soma_positivos += numero
        contador_positivos += 1

    if 50 <= numero <= 100:
        quantidade_50_100 += 1

    if numero < 50:
        quantidade_menor_50 += 1
        if 10 <= numero <= 20:
            quantidade_10_20 += 1

# Calculando a média dos números positivos
media_positivos = soma_positivos / contador_positivos if contador_positivos > 0 else 0

# Calculando as percentagens
percentagem_50_100 = (quantidade_50_100 / contador_total) * 100 if contador_total > 0 else 0
percentagem_10_20 = (quantidade_10_20 / quantidade_menor_50) * 100 if quantidade_menor_50 > 0 else 0

# Mostrando os resultados
print("Quantidade de números inferiores a 35:", quantidade_inferior_35)
print("Média dos números positivos:", media_positivos)
print("Percentagem de números entre 50 e 100:", percentagem_50_100)
print("Percentagem de números entre 10 e 20 entre os números menores que 50:", percentagem_10_20)
