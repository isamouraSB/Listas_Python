#EX38: Escrever um algoritmo que calcula e escreve o produto dos números primos entre 92 e 1478

def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

produto = 1
for numero in range(92, 1479):
    if eh_primo(numero):
        produto *= numero

print(f"O produto dos números primos entre 92 e 1478 é {produto}")
