# Para um estudo envolvendo o nível de multiplicação de bactérias em uma colônia, foi coletado o número de bactérias por dia (em milhares) e pode ser observado a seguir: [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]. 
#Tendo esses valores, faça um código que gere uma lista contendo o percentual de crescimento de bactérias por dia, comparando o número de bactérias em cada dia com o número de bactérias do dia anterior. 
# Dica: para calcular o percentual de crescimento usamos a seguinte equação: 100 * (amostra_atual - amostra_passada) / (amostra_passada).

coloniaBac = [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]

porcentagemCrescimento = []

for i in range (1, len(coloniaBac)):
    porcentagem = 100 * (coloniaBac[i] - coloniaBac[i-1]) / (coloniaBac[i-1])
    porcentagemCrescimento.append(porcentagem)

print (f'porcentagens de crescimento: \n{porcentagemCrescimento}%')