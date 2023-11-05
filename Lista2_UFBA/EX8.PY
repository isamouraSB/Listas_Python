#EX8:Elaborar um programa que lê um conjunto de vários valores inteiros e os coloca em 2 listas conforme forem pares ou ímpares (uma lista para números pares e outra lista para números ímpares). O tamanho da lista é de 5
#posições. Quando alguma lista estiver cheia, ela deverá ser exibida na tela. Cada lista poderá ser preenchida tantas vezes quantas forem necessárias.
#Caso a leitura seja finalizada sem o preenchimento completo de alguma das lista, as listas deverão ser exibidas na tela.

# Inicialize as listas para números pares e ímpares
pares = []
impares = []

# Defina o tamanho máximo para cada lista
tamanho_maximo = 5

while len(pares) < tamanho_maximo or len(impares) < tamanho_maximo:
    valor = int(input("Digite um valor inteiro (ou digite 0 para encerrar): "))
    
    if valor == 0:
        break

    if valor % 2 == 0 and len(pares) < tamanho_maximo:
        pares.append(valor)
        if len(pares) == tamanho_maximo:
            print("Lista de números pares completa:", pares)
    elif len(impares) < tamanho_maximo:
        impares.append(valor)
        if len(impares) == tamanho_maximo:
            print("Lista de números ímpares completa:", impares)

# Exiba as listas, mesmo que não estejam totalmente preenchidas
if pares:
    print("Lista de números pares:", pares)
if impares:
    print("Lista de números ímpares:", impares)
