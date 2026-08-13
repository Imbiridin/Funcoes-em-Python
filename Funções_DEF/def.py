class Automovel:

    def __init__(self, marca, modelo, ano, placa):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.placa = placa

    def get_marca(self):
        return self.modelo

    def get_modelo(self):
        return self.modelo

    def get_ano(self):
        return self.ano

    def get_placa(self):
        return self.placa

    def exibir_informacos(self):
        print(f"Marca: {self.marca}")
        print(f"Marca: {self.modelo}")
        print(f"Marca: {self.ano}")
        print(f"Marca: {self.placa}")

    def dirigir(self):
        print(f"O automóvel {self.marca} do {self.modelo} do ano {self.ano} e da placa {self.placa}.")


Fusca = Automovel("VW", "Fusca", "1977", "ipt-9076")

Fusca.exibir_informacos()

Fusca.dirigir()
