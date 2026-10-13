class No:
    """Nó da fila que armazena o nome do paciente."""
    def __init__(self, nome):
        self.nome = nome
        self.prox = None


class FilaAtendimento:
    """Fila encadeada de pacientes de uma clínica."""

    def __init__(self):
        self.inicio = None
        self.fim = None
        self._tamanho = 0

    # ---------- Verificar se está vazia ----------
    def esta_vazia(self):
        return self.inicio is None

    # ---------- Inserir paciente no final ----------
    def insere(self, nome):
        novo = No(nome)

        if self.esta_vazia():
            self.inicio = novo
            self.fim = novo
        else:
            self.fim.prox = novo
            self.fim = novo

        self._tamanho += 1

    # ---------- Mostrar todos os pacientes ----------
    def mostra(self):
        if self.esta_vazia():
            print("Não há pacientes aguardando.")
            return

        atual = self.inicio
        while atual is not None:
            print(f"  - {atual.nome}")
            atual = atual.prox

    # ---------- Próximo paciente a ser atendido (peek) ----------
    def proximo(self):
        if self.esta_vazia():
            print("Não há pacientes aguardando.")
            return None
        return self.inicio.nome

    # ---------- Atender (remover) o primeiro paciente ----------
    def atende(self):
        if self.esta_vazia():
            print("Não há pacientes aguardando.")
            return None

        paciente = self.inicio.nome
        self.inicio = self.inicio.prox

        if self.inicio is None:   # fila ficou vazia
            self.fim = None

        self._tamanho -= 1
        print(f"Paciente atendido: {paciente}")
        return paciente

    # ---------- Desafio adicional: tamanho ----------
    def tamanho(self):
        return self._tamanho

    # ---------- Representação visual ----------
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