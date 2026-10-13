class No:
    """Nó padrão da fila."""
    def __init__(self, valor):
        self.valor = valor
        self.prox = None


class Fila:
    """Fila dinâmica (encadeada) com política FIFO."""

    # ---------- Inicialização ----------
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def esta_vazia(self):
        return self.inicio is None

    # ---------- Push: insere no FINAL ----------
    def push(self, valor):
        novo = No(valor)

        if self.esta_vazia():
            # Fila vazia: início e fim apontam para o mesmo nó
            self.inicio = novo
            self.fim = novo
        else:
            # Liga o antigo último nó ao novo e atualiza o fim
            self.fim.prox = novo
            self.fim = novo

        self.tamanho += 1

    # ---------- Pop: remove do INÍCIO ----------
    def pop(self):
        if self.esta_vazia():
            print("Fila vazia! Nada a remover.")
            return None

        valor = self.inicio.valor
        self.inicio = self.inicio.prox

        # Se a fila ficou vazia, o fim também deve virar None
        if self.inicio is None:
            self.fim = None

        self.tamanho -= 1
        return valor

    # ---------- Consulta do primeiro (peek) ----------
    def peek(self):
        if self.esta_vazia():
            return None
        return self.inicio.valor

    # ---------- Representação visual ----------
    def __str__(self):
        elementos = []
        atual = self.inicio
        while atual:
            elementos.append(str(atual.valor))
            atual = atual.prox
        if not elementos:
            return "Fila vazia"
        return "Início -> " + " -> ".join(elementos) + " -> None"

    def __len__(self):
        return self.tamanho
    
    
if __name__ == "__main__":
    fila = Fila()

    print("Fila criada:", fila)
    print("Está vazia?", fila.esta_vazia())
    print()

    # -------- Push --------
    print("--- Inserindo elementos ---")
    for v in [10, 20, 30, 40, 50]:
        fila.push(v)
        print(f"push({v:2}) -> {fila}")

    print("\nPrimeiro da fila (peek):", fila.peek())
    print("Tamanho:", len(fila))
    print()

    # -------- Pop --------
    print("--- Removendo elementos ---")
    while not fila.esta_vazia():
        removido = fila.pop()
        print(f"pop() -> {removido:2} | {fila}")

    print("\nTentando remover de fila vazia:")
    fila.pop()
    print("Fila final:", fila)
    print("Tamanho:", len(fila))