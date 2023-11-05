#EX9: Escreva um programa que leia uma lista G de 20 elementos caractere que
#representa o gabarito de uma prova com 20 questões. A seguir, para cada
#um dos 50 alunos de uma turma, leia o nome e o vetor de respostas (R) do
#aluno, após ler conte o número de acertos desse aluno e mostre o numero
#de acertos e uma mensagem APROVADO, se a nota FINAL for maior ou igual
#a 6 ou mostre o numeros de acertos e uma mensagem de REPROVADO,
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
    
    # Verifique se o aluno foi aprovado ou reprovado
    if nota_final >= 6:
        resultado = "APROVADO"
    else:
        resultado = "REPROVADO"
    
    resultados_alunos.append((nome, acertos, resultado))

# Exiba os resultados para cada aluno
for nome, acertos, resultado in resultados_alunos:
    print(f"{nome}: {acertos} acertos. {resultado}")
