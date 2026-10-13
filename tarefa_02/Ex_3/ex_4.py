class No:
    def __init__(self, valor):
        self.valor = valor
        self.prox = None


class Pilha:
    """Pilha auxiliar usada para inverter a fila."""
    def __init__(self):
        self.topo = None

    def esta_vazia(self):
        return self.topo is None

    def push(self, valor):
        novo = No(valor)          # reaproveita a classe No
        novo.prox = self.topo
        self.topo = novo

    def pop(self):
        if self.esta_vazia():
            return None
        valor = self.topo.valor
        self.topo = self.topo.prox
        return valor


class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def esta_vazia(self):
        return self.inicio is None

    def push(self, valor):
        novo = No(valor)
        if self.esta_vazia():
            self.inicio = novo
            self.fim = novo
        else:
            self.fim.prox = novo
            self.fim = novo
        self.tamanho += 1

    def pop(self):
        if self.esta_vazia():
            print("Fila vazia! Nada a remover.")
            return None
        valor = self.inicio.valor
        self.inicio = self.inicio.prox
        if self.inicio is None:
            self.fim = None
        self.tamanho -= 1
        return valor

    def peek(self):
        return None if self.esta_vazia() else self.inicio.valor

    def imprimir(self):
        if self.esta_vazia():
            print("Fila vazia")
            return
        atual = self.inicio
        while atual is not None:
            print(f"[{atual.valor}]", end=" ")
            atual = atual.prox
        print()

    # ---------- Inverter ----------
    def inverter(self):
        """Inverte a ordem dos elementos da fila usando uma pilha auxiliar."""
        if self.esta_vazia():
            return  # nada a inverter

        pilha_aux = Pilha()

        # Passo 1: esvazia a fila empilhando tudo
        while not self.esta_vazia():
            pilha_aux.push(self.pop())

        # Passo 2: desempilha e enfileira de volta (ordem invertida)
        while not pilha_aux.esta_vazia():
            self.push(pilha_aux.pop())


# ---------------- Programa principal ----------------
if __name__ == "__main__":

    fila = Fila()

    print("=== Fila original ===")
    for v in [1, 4, 5, 2]:
        fila.push(v)
    fila.imprimir()

    print("\n=== Invertendo ===")
    fila.inverter()
    fila.imprimir()

    print("\n=== Testando com mais elementos ===")
    fila2 = Fila()
    for v in [10, 20, 30, 40, 50, 60]:
        fila2.push(v)
    print("Antes:  ", end="")
    fila2.imprimir()
    fila2.inverter()
    print("Depois: ", end="")
    fila2.imprimir()

    print("\n=== Testando com fila vazia ===")
    fila3 = Fila()
    fila3.inverter()
    print("OK — não quebrou.")