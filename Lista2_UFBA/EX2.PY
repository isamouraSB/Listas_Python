#EX2: Escreva um programa que receba uma listade de 10 inteiros via teclado, em seguida o programa deve solicitar um número e informar se o número também está na lista ou não.

lista = []
for i in range(10):
    numero = int(input("Digite um número: "))
    lista.append(numero)

numero_solicitado = int(input("Digite um número para verificar se está na lista: "))
if numero_solicitado in lista:
    print("O número está na lista.")
else:
    print("O número não está na lista.")
