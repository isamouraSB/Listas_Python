#EX6: Escreva um programa que faça um cadastro de clientes. Seu programa deve [Entrada]: receber os seguintes dados do usuário: 
# 1) o nome completo; 2) o RG do cliente; 3) o CPF e; 4) o telefone do cliente. 
# [Processamento]: Seu programa deve armazenar todos os dados em uma ÚNICA LISTA. 
# [Saída]: AO FINAL, SOMENTE AO FINAL, Seu programe deve mostrar (um cliente por linha): a) o nome completo do paciente, b) O RG; c) o CPF e; d) o telefone do cliente. 
# Obs: o usuário deve fazer esse procedimento para quantos clientes ele quiser.
#1 a norma de um vetor é a raiz quadrada da soma de seus elementos
#2 o vetor soma é a soma de cada elemento
#Dica: voce pode observar que cada cliente possui 4 informações, portanto, você pode usar isso a seu favor para fazer a impressão dos dados de cada cliente por linha.

clientes = []

while True:
    continuar = input("Deseja adicionar um cliente? (s/n): ")
    if continuar.lower() != 's':
        break

    nome = input("Digite o nome completo do cliente: ")
    rg = input("Digite o RG do cliente: ")
    cpf = input("Digite o CPF do cliente: ")
    telefone = input("Digite o telefone do cliente: ")

    clientes.append([nome, rg, cpf, telefone])

for cliente in clientes:
    print(f"Nome completo do cliente: {cliente[0]}")
    print(f"RG: {cliente[1]}")
    print(f"CPF: {cliente[2]}")
    print(f"Telefone: {cliente[3]}\n")
