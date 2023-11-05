#EX10: Escreva um programa que leia uma lista G de 20 elementos caractere que
#representa o gabarito de uma prova com 20 questões. A seguir, para cada
#um dos 50 alunos de uma turma, leia o nome e o vetor de respostas (R) do
#aluno, após ler conte o número de acertos e ARMAZENE o nome e a NOTA
#FINAL desse aluno. APÓS processar a contagem para os 50 alunos, mostre
#o nome do aluno e a NOTA FINAL seguida da mensagem APROVADO, se a
#nota FINAL for maior ou igual a 6 ou seguida da mensagem REPROVADO,
#caso contrário. Cada questão correta vale 0,5 ponto.

# Leia o gabarito da prova com 20 questões
gabarito = input("Digite o gabarito da prova (20 caracteres): ")

# Inicialize uma lista vazia para armazenar os resultados dos alunos
resultados_alunos = []

# Loop para ler os resultados dos 50 alunos
for i in range(50):
    nome = input(f"Digite o nome do aluno {i + 1}: ")
    respostas_aluno = input(f"Digite as respostas do aluno (20 caracteres): ")
    
    # Inicialize a contagem de acertos para este aluno
    acertos = 0
    
    # Compare as respostas do aluno com o gabarito
    for j in range(20):
        if respostas_aluno[j] == gabarito[j]:
            acertos += 1
    
    # Calcule a nota final do aluno
    nota_final = acertos * 0.5
    
    # Armazene o nome e a nota final na lista de resultados
    resultados_alunos.append((nome, nota_final))

# Exiba os resultados para cada aluno
for nome, nota_final in resultados_alunos:
    resultado = "APROVADO" if nota_final >= 6 else "REPROVADO"
    print(f"{nome}: Nota Final: {nota_final}. {resultado}")
