#EX29: Foi feita uma pesquisa entre os habitantes de uma região, Foram coletados os dados de idade, sexo (M/F) e salário. Faça um programa que calcule e mostre:
#a) a média dos salários do grupo,
#b) a maior e a menor idade do grupo:
#c) a quantidade de mulheres com salário até R$ 200,00;
#d) a idade e o sexo da pessoa que possui o menor salário.
#Finalize a entrada de dados ao ser digitada uma idade negativa.

# Inicializando as variáveis
soma_salarios = 0
contador = 0
maior_idade = -1
menor_idade = float('inf')
mulheres_salario_200 = 0
menor_salario = float('inf')
idade_menor_salario = -1
sexo_menor_salario = ''

# Coletando os dados
while True:
    idade = int(input("Digite a idade (ou um valor negativo para sair): "))
    if idade < 0:
        break
    sexo = input("Digite o sexo (M para masculino, F para feminino): ")
    salario = float(input("Digite o salário: "))

    soma_salarios += salario
    contador += 1

    if idade > maior_idade:
        maior_idade = idade
    if idade < menor_idade:
        menor_idade = idade

    if sexo == 'F' and salario <= 200:
        mulheres_salario_200 += 1

    if salario < menor_salario:
        menor_salario = salario
        idade_menor_salario = idade
        sexo_menor_salario = sexo

# Calculando a média dos salários
media_salarios = soma_salarios / contador if contador > 0 else 0

# Mostrando os resultados
print("Média dos salários do grupo:", media_salarios)
print("Maior idade do grupo:", maior_idade)
print("Menor idade do grupo:", menor_idade)
print("Quantidade de mulheres com salário até R$ 200,00:", mulheres_salario_200)
print("Idade e sexo da pessoa com o menor salário:", idade_menor_salario, sexo_menor_salario)
