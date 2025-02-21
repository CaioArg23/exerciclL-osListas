#Faça um programa que, ao inserir um número qualquer, cria uma lista contendo todos os números primos entre 1 e o número digitado.

n1 = int(input('digite um número que vou exibir todos os números primos até ele : '))

if n1 > 1:
    print ("2")

for numeros in range(2,n1):
    if numeros % 2 == 1:
         print (numeros)

contadorn1 = 0
while n1 > 2:
    contadorn1 = contadorn1 +1
    print (n1)
    if contadorn1 == 1:
        break
    if n1 == 2:
        break