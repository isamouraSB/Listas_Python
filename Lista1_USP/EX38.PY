#EX38: Faça um programa que apresente o menu de opções a seguir, que permita ao usuário escolher a opção desejada, receba os dados necessários para executar a operação e mostre o resultado. Verificar a possibilidade de opção inválida e não se preocupar com as restri- ções, como salário inválido.
#Menu de opções:
#1. Novo salário
#2. Férias
#3. Décimo terceiro
#4. Sair
#Digite a opção desejada
#Na opção 1: receber o salário de um funcionário, calcular e mostrar o novo salário usando as regras a seguir.
#salário	Percentagem de aumento
#Até R$ 350,00	15%
#De R$ 350,00 a R$ 600,00	10%
#Acima de r$ 600,00	5%
#Na opção 2: receber o salário de um funcionário, calcular e mostrar o valor de suas férias. Sabe-se que as férias equivalem ao seu salário acrescido de .
#Na opção 3: receber o salário de um funcionário e o número de meses de trabalho na empresa, no máximo 12, calcular e mostrar o valor do décimo terceiro. Sabe-se que o décimo terceiro equivale ao seu salário multiplicado pelo número de meses de trabalho dividido por 12.
#Na opção 4: sair do programa.


while True:
    print("Menu de opções:")
    print("1. Novo salário")
    print("2. Férias")
    print("3. Décimo terceiro")
    print("4. Sair")
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        salario = float(input("Informe o salário do funcionário: "))
        if salario <= 350:
            salario += salario * 0.15
        elif salario <= 600:
            salario += salario * 0.10
        else:
            salario += salario * 0.05
        print(f"O novo salário é R$ {salario:.2f}")
    elif opcao == 2:
        salario = float(input("Informe o salário do funcionário: "))
        ferias = salario + salario / 3
        print(f"O valor das férias é R$ {ferias:.2f}")
    elif opcao == 3:
        salario = float(input("Informe o salário do funcionário: "))
        meses = int(input("Informe o número de meses de trabalho na empresa: "))
        decimo_terceiro = salario * meses / 12
        print(f"O valor do décimo terceiro é R$ {decimo_terceiro:.2f}")
    elif opcao == 4:
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida.")
