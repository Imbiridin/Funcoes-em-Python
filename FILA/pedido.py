from fila_pedido import Fila

pedido = Fila()
continuar = True

while(continuar):
    opcao = int(input("DIGITE: [1]ADD PEDIDO | [2]REMOVER PEDIDO | [0] SAIR: "))
    match opcao:
        case 1:
            numero = int(input("Informe o número do pedido: "))
            cliente = input("Informe o nome do cliente: ")
            prato = input("Digite o nome do produto: ")
            pedido.insere(numero,cliente,prato)
            print(pedido)
        case 2:
            pedido.remove()
            print(pedido)
        case 0:
            continuar = False
            print("Obrigado por usar nossos serviços!")
            
print(pedido)
