class Pessoa:

    lista = []

    def __init__(self, nome, cpf, idade, genero, email):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.genero = genero
        self.email = email
        Pessoa.lista.append(self)

    def get_nome(self):
        return self.nome

    def get_cpf(self):
        return self.cpf

    def get_idade(self):
        return self.idade

    def get_genero(self):
        return self.genero

    def get_email(self):
        return self.email

    def exibir(self):
        print(f"O seu nome: {self.nome}")
        print(f"O CPF: {self.cpf}")
        print(f"A idade: {self.idade}")
        print(f"O genero: {self.genero}")
        print(f"O e-mail: {self.email}")

    @classmethod
    def cadastro(cls):
        for cadastros in cls.lista:
            print("-"*30)
            cadastros.exibir()
            print("-"*30)

while True:

    pessoa_1 = Pessoa(
        input("Digite o seu nome: "),
        int(input("Digite o CPF: ")),
        int(input("Digite a sua idade: ")),
        input("Digite o seu genero: "),
        input("Digite o seu e-mail: "),
    )

    continuar =input("Deseja continuar?(s/n): ").lower()

    if continuar == 'n':
        break
    elif continuar == 's':
        continue
    else:
        print("Não entendi nada!")

Pessoa.cadastro()