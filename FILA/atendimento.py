from fila_atendimento import Fila

clientes = Fila()
continuar = True

while(continuar):
    opcao = int(input("DIGITE: [1]CADASTRAR | [2]REMOVER | [0] SAIR: "))
    match opcao:
        case 1:
            clientes.insere(input("Informe o nome do cliente: "))
            print(clientes)
        case 2:
            clientes.remove()
            print(clientes)
        case 0:
            continuar = False
            print("Obrigado por usar nossos serviços!")
            break
print(clientes)
