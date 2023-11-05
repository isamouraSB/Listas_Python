#EX11: Escreva um algoritmo que leia um número n (número de termos de uma progressão aritmética), a1 ( o primeiro termo da progressão) e r (a razão da progressão) e escreva os n termos desta progressão, bem como a soma dos elementos.

n = int(input("Digite o número de termos da progressão aritmética: "))
a1 = int(input("Digite o primeiro termo da progressão aritmética: "))
r = int(input("Digite a razão da progressão aritmética: "))

termos = [a1 + r*i for i in range(n)]
soma = sum(termos)

print(f"Os {n} termos da progressão aritmética são: {termos}")
print(f"A soma dos termos é: {soma}")
