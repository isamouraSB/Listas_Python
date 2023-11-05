#EX34: Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:
#FAÇA UM PROGRAMA QUE calcule e mostre:
#a-	O total de votos para cada candidato;
#b-	O total de votos nulos;
#c-	O total de votos brancos;
#d-	A percentagem de votos nulos sobre o total de votos;
#e-	A percentagem de votos em branco sobre o total de votos;
#Para finalizar o conjunto de votos, tem-se o valor zero.

votos = [0, 0, 0, 0, 0, 0]  # Inicializa a lista de votos

voto = int(input("Informe o voto (0 para sair): "))
while voto != 0:
    if 1 <= voto <= 6:
        votos[voto - 1] += 1
    else:
        print("Voto inválido.")
    voto = int(input("Informe o voto (0 para sair): "))

total_votos = sum(votos)
print("Total de votos para cada candidato:")
for i in range(4):
    print(f"Candidato {i + 1}: {votos[i]} votos")

print(f"Total de votos nulos: {votos[4]}")
print(f"Total de votos em branco: {votos[5]}")

if total_votos > 0:
    print(f"Percentual de votos nulos sobre o total de votos: {votos[4] / total_votos * 100:.2f}%")
    print(f"Percentual de votos em branco sobre o total de votos: {votos[5] / total_votos * 100:.2f}%")
else:
    print("Não houve votação.")
