#EX35: Faça um programa que receba como entrada uma lista de números positivos ou negativos, terminada com o número zero. O programa deve fornecer como saída a soma dos números positivos, a soma dos números negativos e a soma das duas somas parciais.

# Inicializando as variáveis
soma_positivos = 0
soma_negativos = 0

# Coletando os números
while True:
    numero = float(input("Digite um número (ou 0 para sair): "))
    if numero == 0:
        break

    if numero > 0:
        soma_positivos += numero
    else:
        soma_negativos += numero

# Calculando a soma das duas somas parciais
soma_total = soma_positivos + soma_negativos

# Mostrando os resultados
print("Soma dos números positivos:", soma_positivos)
print("Soma dos números negativos:", soma_negativos)
print("Soma das duas somas parciais:", soma_total)
