#EX39: Escrever um algoritmo que gera e escreve os 5 primeiros números perfeitos. Um número perfeito é aquele que é igual a soma dos seus divisores. (Ex.: 6 = 1+2+3; 28=1+2+4+7+14 etc)

def eh_perfeito(n):
    soma_divisores = sum(i for i in range(1, n) if n % i == 0)
    return soma_divisores == n

numeros_perfeitos = []
i = 1
while len(numeros_perfeitos) < 5:
    if eh_perfeito(i):
        numeros_perfeitos.append(i)
    i += 1

print("Os 5 primeiros números perfeitos são:", numeros_perfeitos)
