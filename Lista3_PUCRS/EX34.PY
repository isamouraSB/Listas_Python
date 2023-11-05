#EX34: Escrever um algoritmo que leia 5 conjuntos de 2 valores, o primeiro representando o número de um aluno, e o segundo representando a sua altura
# em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e do mais baixo, junto com suas alturas.

alunos = []
for _ in range(5):
    numero = int(input("Digite o número do aluno: "))
    altura = float(input("Digite a altura do aluno em centímetros: "))
    alunos.append((numero, altura))

# Encontrando o aluno mais alto e o mais baixo
mais_alto = max(alunos, key=lambda aluno: aluno[1])
mais_baixo = min(alunos, key=lambda aluno: aluno[1])

print(f"O aluno mais alto é o número {mais_alto[0]} com {mais_alto[1]} cm.")
print(f"O aluno mais baixo é o número {mais_baixo[0]} com {mais_baixo[1]} cm.")

