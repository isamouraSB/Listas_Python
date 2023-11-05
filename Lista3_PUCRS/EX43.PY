#EX43: Fazer um algoritmo que leia 5 grupos de 4 valores (A,B,C,D) e mostre-os na ordem lida. Em seguida, ordene-os em ordem decrescente e mostre-os novamente, já ordenados.

# Lista para armazenar os grupos de valores
grupos = []

# Ler os 5 grupos de valores
for i in range(5):
    grupo = []
    for j in range(4):
        valor = float(input(f"Digite o valor {j + 1} do grupo {i + 1}: "))
        grupo.append(valor)
    grupos.append(grupo)

# Mostrar os grupos na ordem lida
print("Grupos na ordem lida:")
for grupo in grupos:
    print(grupo)

# Ordenar os grupos em ordem decrescente
grupos_ordenados = sorted(grupos, key=lambda grupo: sum(grupo), reverse=True)

# Mostrar os grupos ordenados em ordem decrescente
print("\nGrupos ordenados em ordem decrescente:")
for grupo in grupos_ordenados:
    print(grupo)
