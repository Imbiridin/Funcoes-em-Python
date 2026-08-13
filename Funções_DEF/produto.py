class Mercado:

    lista_de_compras = []

    def __init__(self, marca, tipo, validade, preco):
        self.marca = marca
        self.tipo = tipo
        self.validade = validade
        self.preco = preco
        Mercado.lista_de_compras.append(self)

    def get_marca(self):
        return self.marca
    
    def get_tipo(self):
        return self.tipo

    def get_validade(self):
        return self.validade

    def get_preco(self):
        return self.preco


    def exibir(self):
        print(f"A marca: {self.marca}")
        print(f"O tipo: {self.tipo}")
        print(f"A validade: {self.validade}")
        print(f"O preço: {self.preco}")

    @classmethod
    def produtos(cls):
        for produto in cls.lista_de_compras:
            produto.exibir()
            print("-"*30)



while True:
    caixa = Mercado(
        input("Digite a marca do produto: "),
        input("Digite o tipo do produto: "),
        input("Digite a validade do produto: "),
        float(input("Digite a preço do produto: ")),
    )

    continuar =input("Deseja continuar?(s/n): ").lower()

    if continuar == 'n':
        break
    elif continuar == 's':
        continue
    else:
        print("Não entendi nada!")


Mercado.produtos()