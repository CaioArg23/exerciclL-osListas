#Um instituto de meteorologia deseja fazer um estudo de temperatura média de cada mês do ano. 
# Para isso, você precisa fazer um código que colete e armazene essas temperaturas médias em uma lista. 
# Depois, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual e em que mês elas ocorreram, 
# mostrando os meses por extenso (Janeiro, Fevereiro, etc.).

temperaturas_mensais = []
for i in range(0,12):
  temperaturas_mensais.append(float(input(f'Digite a média de temperatura do mês {i+1}: ')))
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

media_anual = sum(temperaturas_mensais) / len(temperaturas_mensais)

print('Temperaturas acima da média em: ')
for i in range(0,12):
  if temperaturas_mensais[i] > media_anual:

    print(meses[i])