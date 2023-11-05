#EX48: Faça um algoritmo que mostre os conceitos finais dos alunos de uma classe de 75 alunos, considerando (use o comando CASO):
#a) os dados de cada aluno (número de matrícula e nota numérica final) serão fornecidos pelo usuário
#b) a tabela de conceitos segue abaixo:


# Lista para armazenar os dados dos alunos
alunos = []

for _ in range(75):
    # Lendo o número de matrícula e a nota numérica final de cada aluno
    matricula = input("Digite o número de matrícula do aluno: ")
    nota = float(input("Digite a nota numérica final do aluno: "))
    
    # Determinando o conceito do aluno
    if 0.0 <= nota <= 4.9:
        conceito = 'D'
    elif 5.0 <= nota <= 6.9:
        conceito = 'C'
    elif 7.0 <= nota <= 8.9:
        conceito = 'B'
    elif 9.0 <= nota <= 10.0:
        conceito = 'A'
    
    # Adicionando os dados na lista de alunos
    alunos.append((matricula, conceito))

# Mostrando os conceitos finais dos alunos
for matricula, conceito in alunos:
    print(f"Aluno {matricula}: Conceito {conceito}")
