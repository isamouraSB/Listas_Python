#EX1:Escreva um programa que receba uma lista de 10 inteiros via teclado e 
#imprima todo a lista em na mesma linha

lista = []
for i in range(10):
    numero = int(input("Digite um número: "))
    lista.append(numero)

print(" ".join(map(str, lista)))
