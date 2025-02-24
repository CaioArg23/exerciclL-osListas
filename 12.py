#Uma pesquisa de mercado foi feita para decidir qual design de marca infantil mais agrada as crianças.
#A pesquisa foi feita e o votos computados podem ser observados abaixo:

'''
Tabela de votos da marca
Design 1 - 1334 votos
Design 2 - 982 votos
Design 3 - 1751 votos
Design 4 - 210 votos
Design 5 - 1811 votos
'''
#Adapte os dados fornecidos para uma estrutura de dicionário. 
# A partir dele, informe o design vencedor e a porcentagem de votos recebidos.

votos = {'Design 1': 1334, 'Design 2': 982, 'Design 3': 1751, 'Design 4': 210, 'Design 5': 1811}

total_votos = 0 
vencedor = '' 
voto_vencedor = 0 

for design, voto_desing in votos.items():

  total_votos += voto_desing
  
  if voto_desing > voto_vencedor:
    voto_vencedor = voto_desing
    vencedor = design

porcentagem = 100 * (voto_vencedor) / (total_votos)

print(f'{vencedor} é o vencedor: ')
print(f'Porcentagem de votos: {porcentagem}%')