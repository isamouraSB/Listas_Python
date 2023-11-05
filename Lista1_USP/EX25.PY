#EX25: O sistema de avaliação de uma determinada disciplina obedece aos seguintes critérios:
#•	Durante o semestre são dadas três notas;
#•	A nota final é obtida pela média aritmética das três notas
#•	É considerado aprovado o aluno que obtiver a nota final superior ou igual a 6 e que tiver comparecido a um de 40 aulas.
#Faça um programa que
#•	Leia um conjunto de dados contendo o número da matrícula, as três notas e a frequência (número de aulas frequentadas) de dez alunos.
#Calcule e mostre:
#•	Para cada aluno o número da matrícula, a nota final e a mensagem (aprovado ou reprovado):
#•	A maior e a menor nota da turma:
#•	O total de alunos reprovados;
#•	A percentagem de alunos reprovados por frequência abaixo da mínima necessária.

# Inicializando as variáveis
maior_nota = -1
menor_nota = float('inf')
total_reprovados = 0
reprovados_frequencia = 0

# Coletando os dados de 10 alunos
for i in range(10):
    matricula = input("Digite o número da matrícula: ")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    frequencia = int(input("Digite o número de aulas frequentadas: "))

    # Calculando a nota final
    nota_final = (nota1 + nota2 + nota3) / 3

    # Verificando se o aluno foi aprovado ou reprovado
    if nota_final >= 6 and frequencia >= 40:
        status = "Aprovado"
    else:
        status = "Reprovado"
        total_reprovados += 1
        if frequencia < 40:
            reprovados_frequencia += 1

    # Atualizando a maior e a menor nota
    if nota_final > maior_nota:
        maior_nota = nota_final
    if nota_final < menor_nota:
        menor_nota = nota_final

    # Mostrando os resultados para o aluno
    print("Número da matrícula:", matricula)
    print("Nota final:", nota_final)
    print("Status:", status)

# Calculando a percentagem de alunos reprovados por frequência
percentagem_reprovados_frequencia = (reprovados_frequencia / 10) * 100

# Mostrando os resultados para a turma
print("Maior nota da turma:", maior_nota)
print("Menor nota da turma:", menor_nota)
print("Total de alunos reprovados:", total_reprovados)
print("Percentagem de alunos reprovados por frequência:", percentagem_reprovados_frequencia)

