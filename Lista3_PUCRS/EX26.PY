#EX26: Escreva um algoritmo que gere o números de 1000 a 1999 e escreva aqueles que dividido por 11 dão resto igual a 5.

# Gerando os números de 1000 a 1999
for numero in range(1000, 2000):
    # Verificando se o número dividido por 11 dá resto igual a 5
    if numero % 11 == 5:
        print(numero)
