#EX10: Faça um programa que mostre a tabuada de 1 a 10.

num = int(input("Informe um número: "))
for x in range(1,11):     
    tabuada = num * x     
    print(num, "x", x,"=", tabuada)  

