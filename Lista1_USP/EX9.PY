#EX9: Faça um programa que receba um número e que calcule e mostre a tabuada desse número.

num = int(input("Digite um número para saber sua tabuada: ")) 
for x in range(0,11):     
    tabuada = num * x     
    print(num, "x", x,"=", tabuada) 
    