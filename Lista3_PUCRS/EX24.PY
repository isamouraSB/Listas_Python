#EX24: Faça um algoritmo que determine e escreva:
#- a maior idade dos habitantes
#- a quantidade de indivíduos do sexo feminino cuja idade está entre 18 e 35 anos inclusive e que tenham olhos verdes e cabelos louros.
#O final do conjunto de habitantes é reconhecido pelo valor -1 entrada como idade.

# Lista para armazenar os dados dos habitantes
habitantes = []

while True:
    # Coletando os dados de cada habitante
    idade = int(input("Digite a idade (ou -1 para terminar): "))
    
    # Verificando se o usuário quer terminar
    if idade == -1:
        break
    
    sexo = input("Digite o sexo (masculino ou feminino): ")
    cor_olhos = input("Digite a cor dos olhos (azuis, verdes ou castanhos): ")
    cor_cabelos = input("Digite a cor dos cabelos (louros, castanhos ou pretos): ")
    
    # Adicionando os dados na lista de habitantes
    habitantes.append({
        "idade": idade,
        "sexo": sexo,
        "cor_olhos": cor_olhos,
        "cor_cabelos": cor_cabelos
    })

# Determinando a maior idade dos habitantes
maior_idade = max(habitante['idade'] for habitante in habitantes)
print(f"A maior idade entre os habitantes é {maior_idade} anos.")

# Determinando a quantidade de indivíduos do sexo feminino cuja idade está entre 18 e 35 anos inclusive e que tenham olhos verdes e cabelos louros
quantidade = sum(1 for habitante in habitantes if habitante['sexo'] == 'feminino' and 18 <= habitante['idade'] <= 35 and habitante['cor_olhos'] == 'verdes' and habitante['cor_cabelos'] == 'louros')
print(f"A quantidade de indivíduos do sexo feminino cuja idade está entre 18 e 35 anos inclusive e que tenham olhos verdes e cabelos louros é {quantidade}.")
