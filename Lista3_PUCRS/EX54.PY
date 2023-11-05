#EX54: Faça uma algoritmo que receba 2 numeros e divida o intervalo entre eles em 3 partes iguais. Obs. Faça a consistência para que os extremos não sejam iguais


# Função para dividir o intervalo entre dois números em três partes iguais
def dividir_em_tres_partes(Numero1, Numero2):
    # Verifique se os extremos não são iguais
    if Numero1 == Numero2:
        return "Os números de entrada são iguais."

    # Ordene os números
    menor = min(Numero1, Numero2)
    maior = max(Numero1, Numero2)

    # Calcule o tamanho do intervalo
    tamanho_intervalo = (maior - menor) / 3

    # Calcule os pontos de divisão
    ponto1 = menor + tamanho_intervalo
    ponto2 = ponto1 + tamanho_intervalo

    return (menor, ponto1, ponto2, maior)

# Ler os números de entrada
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Chame a função para dividir o intervalo em três partes iguais
resultado = dividir_em_tres_partes(numero1, numero2)

# Exiba o resultado
if isinstance(resultado, tuple):
    menor, ponto1, ponto2, maior = resultado
    print(f"Os pontos de divisão são: {menor}, {ponto1}, {ponto2}, {maior}")
else:
    print(resultado)
