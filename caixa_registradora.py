# Exercício - O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de convêniencias. Faça um programa que implemente uma caixa
# registradora rudimentar. O programa deverá receber um npumero desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador
# para indicar o final da compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor
# do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:

#Definindo uma função para o espaço entre o encerramento e a continuação da caixa registradora!
def espaco():
  print("\n"*3)

while True:
  print("------------Convêniencias Tabajara------------")
  print("-----------Digite (-0) para encerrar-----------")
  n = 1
  total = 0

  while True:
    produto = float(input("Valor do Produto {}: R$ ".format(n)))
    n += 1
    total += produto
    if produto == 0:
      break

  print("------------------------------------")

  print("Valor Total da Compra: R$ {:.2f}".format(total))
  dinheiro = float(input("Dinheiro do cliente: R$ "))
  print("Troco: R$ {:.2f}".format(dinheiro - total))

  print("------------------------------------")

  reset = input("Se deseja reiniciar digite 0, caso deseje encerrar digite 1:")
  if reset == "0":
    espaco()
    continue

  else:
    espaco()
    print("------------------------------------")
    print("Encerrando o caixa...")
    break
