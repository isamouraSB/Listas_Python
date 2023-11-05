# EX1:Faça um programa que verifique e mostre os números entre 1000 e 2000(inclusive) que quando divididos por 11 produzam resto igual a 5: 
 
for x in range(1000,2001):     
    if x % 11 == 5: 
        print(x) 
