#EX6: Em uma eleição presidencial existem quatro candidatos. Os votos são informados através de códigos. Os dados utilizados para a contagem dos votos obedecem à seguinte codificação:
#- 1,2,3,4 = voto para os respectivos candidatos;
#- 5 = voto nulo;
#- 6 = voto em branco;
#Elabore um algoritmo que leia o código do candidado em um voto. Calcule e escreva:
#- total de votos para cada candidato;
#- total de votos nulos;
#- total de votos em branco;
#Como finalizador do conjunto de votos, tem-se o valor 0

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
