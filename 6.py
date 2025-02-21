#Escreva um programa que peça uma data informando o dia, mês e ano e determine se ela é válida para uma análise
dia = int(input('digite o dia: '))
mes = int(input('digite o mes: '))
ano = int(input('digite o ano: '))

listaDia_mes_ano = []

if dia > 31:
        print ('dê um dia válido')
if mes > 12:
        print ('dê um mês valido')

else:
    listaDia_mes_ano.extend([dia,mes,ano])
    print (listaDia_mes_ano)