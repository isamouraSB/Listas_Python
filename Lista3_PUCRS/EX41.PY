#EX41: Faça um algoritmo que leia as três notas de 50 alunos de uma turma. Para cada aluno, calcule a média ponderada, como segue: MP = ( n1*2 + n2*4 + n3*3 ) / 10
# Além disso, calcule a média geral da turma. Mostre a média de cada aluno e uma mensagem "Aprovado", caso a média seja maior ou igual a sete, e uma mensagem
# "Reprovado", caso contrário. Ao final, mostre a média geral.

# Inicialize a variável para a média geral da turma
media_geral = 0

# Loop para ler as notas de 50 alunos
for aluno in range(1, 51):
    n1 = float(input(f"Nota 1 do aluno {aluno}: "))
    n2 = float(input(f"Nota 2 do aluno {aluno}: "))
    n3 = float(input(f"Nota 3 do aluno {aluno}: "))
    
    # Calcule a média ponderada
    media_ponderada = (n1 * 2 + n2 * 4 + n3 * 3) / 10

    # Adicione a média ponderada à média geral
    media_geral += media_ponderada

    # Verifique se o aluno foi aprovado ou reprovado
    if media_ponderada >= 7:
        resultado = "Aprovado"
    else:
        resultado = "Reprovado"
    
    print(f"Aluno {aluno}: Média Ponderada = {media_ponderada:.2f} ({resultado})")

# Calcule a média geral da turma
media_geral /= 50

print(f"Média Geral da Turma: {media_geral:.2f}")
