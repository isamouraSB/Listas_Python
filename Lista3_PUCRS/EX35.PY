#EX35: Escrever um algoritmo que leia um conjunto de 50 informações contendo, cada uma delas, a altura e o sexo de uma pessoa (código=1, masculino código=2, feminino), calcule e mostre o seguinte:
#a) a maior e a menor altura da turma
#b) a média da altura das mulheres
#c) a média da altura da turma.

# Lista para armazenar as informações
pessoas = []

for _ in range(50):
    # Lendo a altura e o sexo de cada pessoa
    altura = float(input("Digite a altura da pessoa: "))
    sexo = int(input("Digite o sexo da pessoa (1 para masculino, 2 para feminino): "))
    
    # Adicionando as informações na lista de pessoas
    pessoas.append((altura, sexo))

# Calculando a maior e a menor altura da turma
maior_altura = max(pessoa[0] for pessoa in pessoas)
menor_altura = min(pessoa[0] for pessoa in pessoas)

print(f"A maior altura da turma é {maior_altura} m.")
print(f"A menor altura da turma é {menor_altura} m.")

# Calculando a média da altura das mulheres
altura_mulheres = [pessoa[0] for pessoa in pessoas if pessoa[1] == 2]
media_altura_mulheres = sum(altura_mulheres) / len(altura_mulheres)

print(f"A média da altura das mulheres é {media_altura_mulheres} m.")

# Calculando a média da altura da turma
altura_turma = [pessoa[0] for pessoa in pessoas]
media_altura_turma = sum(altura_turma) / len(altura_turma)

print(f"A média da altura da turma é {media_altura_turma} m.")
