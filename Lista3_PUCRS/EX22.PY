#22. Foi feita uma pesquisa entre os habitantes de uma região. Foram coletados os dados de idade, sexo (M/F) e salário. Faça um algoritmo que informe:
#a) a média de salário do grupo;
#b) maior e menor idade do grupo;
#c) quantidade de mulheres com salário até R$100,00.
#Encerre a entrada de dados quando for digitada uma idade negativa. (Use o comando enquanto-faça e não use vetores ou matrizes)

soma_salarios = 0
maior_idade = float('-inf')
menor_idade = float('inf')
contagem_mulheres_salario_ate_100 = 0

while True:
    idade = int(input("Digite a idade (ou idade negativa para sair): "))
    
    if idade < 0:
        break

    sexo = input("Digite o sexo (M/F): ")
    salario = float(input("Digite o salário: "))

    soma_salarios += salario
    if idade > maior_idade:
        maior_idade = idade
    if idade < menor_idade:
        menor_idade = idade

    if sexo == 'F' and salario <= 100.00:
        contagem_mulheres_salario_ate_100 += 1

if contagem_mulheres_salario_ate_100 > 0:
    media_salario = soma_salarios / (idade - 1)
else:
    media_salario = 0

print(f"Média de salário do grupo: {media_salario}")
print(f"Maior idade do grupo: {maior_idade}")
print(f"Menor idade do grupo: {menor_idade}")
print(f"Quantidade de mulheres com salário até R$100,00: {contagem_mulheres_salario_ate_100}")
