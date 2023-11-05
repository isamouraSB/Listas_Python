#EX14: Escrever um algoritmo que leia um número não determinado de valores e calcule a média aritmética dos valores lidos, a quantidade de valores positivos, a quantidade de valores negativos e o percentual de valores negativos e positivos. Mostre os resultados.

valores = []
while True:
    valor = float(input("Digite um valor (0 para sair): "))
    if valor == 0:
        break
    valores.append(valor)

media = sum(valores) / len(valores)
positivos = len([valor for valor in valores if valor > 0])
negativos = len([valor for valor in valores if valor < 0])
percentual_positivos = positivos / len(valores) * 100
percentual_negativos = negativos / len(valores) * 100

print(f"Média aritmética: {media:.2f}")
print(f"Quantidade de valores positivos: {positivos}")
print(f"Quantidade de valores negativos: {negativos}")
print(f"Percentual de valores positivos: {percentual_positivos:.2f}%")
print(f"Percentual de valores negativos: {percentual_negativos:.2f}%")
