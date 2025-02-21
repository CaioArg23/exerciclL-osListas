#Com os mesmos dados da questão anterior, 
# defina quantas compras foram realizadas acima de 3000 reais e calcule a porcentagem quanto ao total de compras.

gastos = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]

contador300 = 0

for numeros in gastos:
    if numeros > 3000:
        contador300 +=1
       

quantidadeGastos = len(gastos)

porcentagemDenumero300 = 100* (contador300) / (quantidadeGastos)

print (f'o numero de compras feitas acima de R$3000,00 foi: {contador300}')
print (f'e a porcentagem de compras feitas acima de R$3000 foi de: {porcentagemDenumero300}%')