#EX23: Foi realizada uma pesquisa de algumas características físicas da população de uma certa região, a qual coletou os seguintes dados referentes a cada habitante para serem analisados:
#- sexo (masculino e feminino)
#- cor dos olhos (azuis, verdes ou castanhos)
#- cor dos cabelos ( louros, castanhos, pretos)
#- idade

# Lista para armazenar os dados dos habitantes
habitantes = []

while True:
    # Coletando os dados de cada habitante
    sexo = input("Digite o sexo (masculino ou feminino): ")
    cor_olhos = input("Digite a cor dos olhos (azuis, verdes ou castanhos): ")
    cor_cabelos = input("Digite a cor dos cabelos (louros, castanhos ou pretos): ")
    idade = int(input("Digite a idade: "))
    
    # Adicionando os dados na lista de habitantes
    habitantes.append({
        "sexo": sexo,
        "cor_olhos": cor_olhos,
        "cor_cabelos": cor_cabelos,
        "idade": idade
    })
    
    # Perguntando se o usuário quer continuar
    continuar = input("Deseja continuar? (s/n): ")
    if continuar.lower() != 's':
        break

# Imprimindo os dados coletados
for i, habitante in enumerate(habitantes, 1):
    print(f"Habitante {i}:")
    print(f"Sexo: {habitante['sexo']}")
    print(f"Cor dos olhos: {habitante['cor_olhos']}")
    print(f"Cor dos cabelos: {habitante['cor_cabelos']}")
    print(f"Idade: {habitante['idade']}")
    print()

