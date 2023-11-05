#EX4:Escreva um programa que:
#  [Entrada]: receba do usuário: 1) o valor base de indenização por um plano de saúde; 2) a idade do paciente indenizado e; 3) o nome completo do paciente. 
#[Processamento]: Seu programa deve calcular o reajuste de indenização sobre o valor base de acordo com a idade do paciente. Seu programa deve aumentar o valor da indenização em: 30% se o paciente tiver até 12 anos; 10% se o paciente tiver idade entre 13 e 49 anos (inclusive); 15%  se o paciente tiver idade entre 50 e 65 anos (inclusive) e; 35% se o paciente tiver idade acima de 65 anos. 
#[Saída]: AO FINAL, SOMENTE AO FINAL, Seu programe deve mostrar (um paciente por linha): o nome do paciente, a idade do paciente e qual foi o valor da indenização reajustado. Obs: o usuário deve fazer
#esse procedimento para quantos clientes ELE QUISER. Dica: voce PODE usar três vetores: um para os nomes, outro para as idades e outro para as indenizações reajustadas.

nomes = []
idades = []
indenizacoes = []

while True:
    continuar = input("Deseja adicionar um paciente? (s/n): ")
    if continuar.lower() != 's':
        break

    nome = input("Digite o nome do paciente: ")
    idade = int(input("Digite a idade do paciente: "))
    indenizacao_base = float(input("Digite o valor base da indenização: "))

    if idade <= 12:
        indenizacao = indenizacao_base * 1.30
    elif 13 <= idade <= 49:
        indenizacao = indenizacao_base * 1.10
    elif 50 <= idade <= 65:
        indenizacao = indenizacao_base * 1.15
    else:
        indenizacao = indenizacao_base * 1.35

    nomes.append(nome)
    idades.append(idade)
    indenizacoes.append(indenizacao)

for nome, idade, indenizacao in zip(nomes, idades, indenizacoes):
    print(f"Nome do paciente: {nome}, Idade: {idade}, Valor da indenização reajustado: R$ {indenizacao:.2f}")
