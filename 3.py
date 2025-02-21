#Faça um código que colete em uma lista 5 números inteiros quaisquer e imprima a lista em ordem crescente. Exemplo: [1,4,7,2,4].
n1 = int(input('digite um número: '))
n2 = int(input('digite um número: '))
n3 = int(input('digite um número: '))
n4 = int(input('digite um número: '))
n5 = int(input('digite um número: '))

numeros = [(n1), (n2), (n3), (n4), (n5)]
numerosEmOrdem = sorted(numeros)  
print(numerosEmOrdem)


