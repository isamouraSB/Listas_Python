#EX7: 7. Escreva um algoritmo que calcule a média aritmética das 3 notas dos alunos de uma classe. O algoritmo deverá ler, além das notas, o código do aluno e deverá ser encerrado quando o código for igual a zero.


alunos = []

while True:
    codigo = int(input("Informe o código do aluno (0 para sair): "))
    if codigo == 0:
        break

    nota1 = float(input("Informe a primeira nota do aluno: "))
    nota2 = float(input("Informe a segunda nota do aluno: "))
    nota3 = float(input("Informe a terceira nota do aluno: "))

    media = (nota1 + nota2 + nota3) / 3
    alunos.append((codigo, media))

for codigo, media in alunos:
    print(f"Código do aluno: {codigo}, média: {media:.2f}")
