#EX0: Escreva um algoritmo que leia o código de um aluno e suas três notas. Calcule a média ponderada do aluno, considerando que o peso para a maior nota seja 4 e para as duas restantes, 3. Mostre o código do aluno, suas três notas, a média calculada e uma mensagem "APROVADO" se a média for maior ou igual a 5 e "REPROVADO" se a média for menor que 5. Repita a operação até que o código lido seja negativo.

while True:
    codigo = int(input("Digite o código do aluno (negativo para sair): "))
    if codigo < 0:
        break

    notas = [float(input(f"Digite a nota {i+1} do aluno: ")) for i in range(3)]
    notas.sort()
    media = (notas[2]*4 + notas[1]*3 + notas[0]*3) / 10

    print(f"Código do aluno: {codigo}")
    print(f"Notas: {notas[0]}, {notas[1]}, {notas[2]}")
    print(f"Média: {media:.2f}")
    if media >= 5:
        print("APROVADO")
    else:
        print("REPROVADO")
