# TODO: Crie uma Função: recomendar_plano para receber o consumo médio mensal:
def recomendar_plano(consumo, plano):
  # TODO: Crie uma Estrutura Condicional para verifica o consumo médio mensal 
  # TODO: Retorne o plano de internet adequado:
  if consumo <= 10:
    plano = 'Plano Essencial Fibra - 50Mbps\n'
    return plano
  elif consumo > 10 and consumo <=20:
    plano = 'Plano Prata Fibra - 100Mbps\n'
    return plano
  plano = 'Plano Premium Fibra - 300Mbps\n'
  return plano

  
# TODO: Retorne o plano de internet adequado:
    
plano = ''
# Solicita ao usuário que insira o consumo médio mensal de dados:
consumo = float(input('Insira o consumo de internet mensal em GB: '))
# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
print(recomendar_plano(consumo, plano))
