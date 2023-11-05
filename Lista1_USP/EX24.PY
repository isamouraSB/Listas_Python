#EX24: Uma firma fez uma pesquisa de mercado para saber se as pessoas gostaram ou não de um novo produto lançado no mercado. Para isso forneceu o sexo do entrevistado e sua resposta (S- Sim ou N- Não). Sabe-se que foram entrevistadas dez pessoas. Faça um programa que calcule e mostre:
#•	O número de pessoas que respondeu sim;
#•	O número de pessoas que respondeu não;
#•	O número de mulheres que respondeu sim;
#•	A percentagem de homens que respondeu não entre todos os homens analisados.

# Inicializando as variáveis
respostas_sim = 0
respostas_nao = 0
mulheres_sim = 0
homens_nao = 0
total_homens = 0

# Coletando os dados de 10 pessoas
for i in range(10):
    sexo = input("Digite o sexo (M para masculino, F para feminino): ")
    resposta = input("Digite a resposta (S para sim, N para não): ")

    if resposta == 'S':
        respostas_sim += 1
        if sexo == 'F':
            mulheres_sim += 1
    elif resposta == 'N':
        respostas_nao += 1
        if sexo == 'M':
            homens_nao += 1

    if sexo == 'M':
        total_homens += 1

# Calculando a percentagem de homens que respondeu não
percentagem_homens_nao = (homens_nao / total_homens) * 100 if total_homens > 0 else 0

# Mostrando os resultados
print("Número de pessoas que respondeu sim:", respostas_sim)
print("Número de pessoas que respondeu não:", respostas_nao)
print("Número de mulheres que respondeu sim:", mulheres_sim)
print("Percentagem de homens que respondeu não:", percentagem_homens_nao)
