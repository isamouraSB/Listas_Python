#EX53: Faça um algoritmo que calcule os 20 primeiros números primos, dados os tres primeiros 1,2 e 3.


# Função para verificar se um número é primo
def is_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Inicialize uma lista para armazenar os números primos encontrados
numeros_primos = [1, 2, 3]

# Comece a busca por números primos a partir de 4 (já temos os três primeiros)
numero = 4

while len(numeros_primos) < 20:
    if is_primo(numero):
        numeros_primos.append(numero)
    numero += 1

# Exiba os 20 primeiros números primos
print("Os 20 primeiros números primos são:")
for primo in numeros_primos:
    print(primo)
