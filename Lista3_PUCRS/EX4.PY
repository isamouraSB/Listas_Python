#EX4: Chico tem 1,50 metro e cresce 2 centímetros por ano, enquanto Zé tem 1,10 metro e cresce 3 centímetros por ano. Construa um algoritmo que calcule e imprima quantos
#anos serão necessários para que Zé seja maior que Chico.

altura_chico = 1.50  # em metros
altura_ze = 1.10  # em metros
anos = 0

while altura_ze <= altura_chico:
    altura_chico += 0.02  # Chico cresce 2 centímetros por ano
    altura_ze += 0.03  # Zé cresce 3 centímetros por ano
    anos += 1

print(f"Serão necessários {anos} anos para que Zé seja maior que Chico.")
