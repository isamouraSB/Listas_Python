#EX46: Foi realizada uma pesquisa de algumas características físicas da população de um certa região. Foram entrevistadas 500 pessoas e coletados os seguintes dados:
#a- sexo: M (masculino) e F (feminino)
#b- cor dos olhos: A (azuis), V (verdes) e C (castanhos)
#c- cor dos cabelos: L (louros), C (castanhos) e P (pretos)
#d- idade
#Deseja-se saber:
# a maior idade do grupo
# A quantidade de indivíduos do sexo feminino, cuja idade está entre 18 e 35 anos e que tenham olhos verdes e cabelos louros

# Variáveis para acompanhar a maior idade e a quantidade de mulheres que atendem aos critérios
maior_idade = -1
quantidade_mulheres = 0

# Loop para ler os dados de 500 pessoas
for pessoa in range(1, 501):
    sexo = input("Digite o sexo (M/F): ")
    cor_olhos = input("Digite a cor dos olhos (A/V/C): ")
    cor_cabelos = input("Digite a cor dos cabelos (L/C/P): ")
    idade = int(input("Digite a idade: "))

    # Verifique a maior idade
    if idade > maior_idade:
        maior_idade = idade

    # Verifique se a pessoa é do sexo feminino, com idade entre 18 e 35 anos, olhos verdes e cabelos louros
    if sexo == 'F' and 18 <= idade <= 35 and cor_olhos == 'V' and cor_cabelos == 'L':
        quantidade_mulheres += 1

# Imprimir os resultados
print(f"Maior idade do grupo: {maior_idade}")
print(f"Quantidade de mulheres com idade entre 18 e 35 anos, olhos verdes e cabelos louros: {quantidade_mulheres}")
