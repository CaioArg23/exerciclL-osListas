
#Para uma seleção de produtos alimentícios, 
# precisamos separar o conjunto de IDs dados por números inteiros sabendo que os produtos com ID par são doces e os com ID ímpar são amargos. 
# Monte um código que colete 10 IDs. Depois, calcule e mostre a quantidade de produtos doces e amargos.

soma1 = 0  
soma2 = 0  

lista = []
for i in range(10):
    id_produto = int(input(f'Digite o ID do produto {i+1}: '))
    lista.append(id_produto)

for id_produto in lista:
    if id_produto % 2 == 0:
        soma1 += 1  
    else:
        soma2 += 1  

print(f'Temos {soma1} doces e {soma2} amargos.')