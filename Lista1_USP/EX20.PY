#20. Faça um programa que receba um conjunto de valores inteiros e positivos e que calcule e mostre o maior e o menor valor do conjunto. Considere que:
#•	Para encerrar a entrada de dados, deve ser digitado o valor zero;
#•	Para valores negativos, deve ser enviada uma mensagem;
#•	Os valores negativos ou iguais a zero não entrarão nos cálculos.

# Inicializando as variáveis
maior_valor = -1
menor_valor = float('inf')

# Coletando os valores
while True:
    valor = int(input("Digite um valor inteiro e positivo (ou 0 para sair): "))
    if valor == 0:
        break
    elif valor < 0:
        print("Valor inválido! Por favor, digite um valor inteiro e positivo.")
    else:
        if valor > maior_valor:
            maior_valor = valor
        if valor < menor_valor:
            menor_valor = valor

# Verificando se algum valor válido foi digitado
if maior_valor == -1 or menor_valor == float('inf'):
    print("Nenhum valor válido foi digitado.")
else:
    # Mostrando o maior e o menor valor
    print("Maior valor:", maior_valor)
    print("Menor valor:", menor_valor)
