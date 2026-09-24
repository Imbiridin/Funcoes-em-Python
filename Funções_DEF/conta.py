class Conta:

    def __init__(self, credito, debito, saldo):
        self.__credito = credito
        self.__debito = debito
        self.__saldo = saldo
        self.__cheque_esepcial = 500

    def get_credito(self):
        return self.__credito

    def get_debito(self):
        return self.__debito

    def get_saldo(self):
        return self.__saldo


    def depositar(self):
        if saldo > 0:

    def sacar(self, valor):
        limite_disponivel = self.__saldo + self.__cheque_especial

        if valor <= limite_disponivel:
            self.__saldo -= valor
            print(f"Saque de {valor} realizado. Novo saldo: {self.__saldo}")
        else:
            print("Saldo insuficiente, mesmo com cheque especial.")


