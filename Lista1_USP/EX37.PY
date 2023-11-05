#EX37: Faça um programa que apresente um menu de opções para o cálculo das seguintes operações entre dois números: adição, subtração, multiplicação e divisão. O programa deve possibilitar ao usuário a escolha da operação desejada, a exibição do resultado e a volta ao menu de opções. O programa só termina quando for escolhida a opção de saída.


while True:
    print("Menu de opções:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 5:
        break

    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))

    if opcao == 1:
        resultado = numero1 + numero2
    elif opcao == 2:
        resultado = numero1 - numero2
    elif opcao == 3:
        resultado = numero1 * numero2
    elif opcao == 4:
        if numero2 != 0:
            resultado = numero1 / numero2
        else:
            print("Erro! Divisão por zero.")
            continue
    else:
        print("Opção inválida!")
        continue

    print("Resultado:", resultado)
