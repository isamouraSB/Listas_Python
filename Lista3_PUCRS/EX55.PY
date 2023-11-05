#EX55: Faça uma algoritmo que receba duas datas e retorne a diferença entre elas em dias.

from datetime import datetime

# Função para calcular a diferença em dias entre duas datas
def diferenca_em_dias(data1, data2):
    data1 = datetime.strptime(data1, '%Y-%m-%d')
    data2 = datetime.strptime(data2, '%Y-%m-%d')
    diferenca = abs((data1 - data2).days)
    return diferenca

# Ler as duas datas no formato 'YYYY-MM-DD'
data1 = input("Digite a primeira data (YYYY-MM-DD): ")
data2 = input("Digite a segunda data (YYYY-MM-DD): ")

# Chamar a função para calcular a diferença em dias
diferenca = diferenca_em_dias(data1, data2)

# Exibir a diferença em dias
print(f"A diferença entre as duas datas é de {diferenca} dias.")
