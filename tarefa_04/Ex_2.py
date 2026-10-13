class No:
    def __init__(self, nome):
        self.nome = nome
        self.prox = None


class FilaAtendimento:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self._tamanho = 0

    def esta_vazia(self):
        return self.inicio is None

    def insere(self, nome):
        novo = No(nome)
        if self.esta_vazia():
            self.inicio = novo
            self.fim = novo
        else:
            self.fim.prox = novo
            self.fim = novo
        self._tamanho += 1

    def mostra(self):
        if self.esta_vazia():
            print("Não há pacientes aguardando.")
            return
        atual = self.inicio
        while atual is not None:
            print(f"  - {atual.nome}")
            atual = atual.prox

    def proximo(self):
        if self.esta_vazia():
            print("Não há pacientes aguardando.")
            return None
        return self.inicio.nome

    def atende(self):
        if self.esta_vazia():
            print("Não há pacientes aguardando.")
            return None
        paciente = self.inicio.nome
        self.inicio = self.inicio.prox
        if self.inicio is None:
            self.fim = None
        self._tamanho -= 1
        print(f"Paciente atendido: {paciente}")
        return paciente

    def tamanho(self):
        return self._tamanho

    def __str__(self):
        if self.esta_vazia():
            return "[None]"
        nomes = []
        atual = self.inicio
        while atual is not None:
            nomes.append(atual.nome)
            atual = atual.prox
        return "[" + " -> ".join(nomes) + " -> None]"


if __name__ == "__main__":
    fila = FilaAtendimento()

    # Inserindo pacientes
    fila.insere("Ana")
    fila.insere("Carlos")
    fila.insere("Mariana")

    print("Fila atual:")
    print(fila)
    print()

    # Atendendo o primeiro paciente
    fila.atende()
    print("\nFila atual:")
    print(fila)
    print()

    # Próximo a ser atendido
    print("Próximo paciente:", fila.proximo())
    print("Quantidade aguardando:", fila.tamanho())
    print()

    # Atendendo mais um
    fila.atende()
    fila.atende()

    # Tentando atender fila vazia
    fila.atende()
    
