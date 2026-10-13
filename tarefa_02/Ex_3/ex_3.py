class No:
    def __init__(self, valor):
        self.valor = valor
        self.prox = None


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

    def buscar(self, valor):
        if self.esta_vazia():
            return -1
        posicao = 1
        atual = self.inicio
        while atual is not None:
            if atual.valor == valor:
                return posicao
            atual = atual.prox
            posicao += 1
        return -1

    # ---------- NOVO: imprimir ----------
    def imprimir(self):
        if self.esta_vazia():
            print("Fila vazia — nada a imprimir.")
            return

        print("Elementos da fila:")
        atual = self.inicio
        posicao = 1
        while atual is not None:
            print(f"  Posição {posicao}: {atual.valor}")
            atual = atual.prox
            posicao += 1

    # ---------- NOVO: imprimir em linha ----------
    def imprimir_linha(self):
        if self.esta_vazia():
            print("Fila vazia")
            return
        atual = self.inicio
        while atual is not None:
            print(atual.valor, end=" ")
            atual = atual.prox
        print()
        
if __name__ == "__main__":
    fila = Fila()

    print("=== Teste 1: fila vazia ===")
    fila.imprimir()
    print()

    print("=== Teste 2: fila com elementos ===")
    for v in [10, 20, 30, 40, 50]:
        fila.push(v)

    fila.imprimir()
    print()

    print("=== Teste 3: imprimir em linha ===")
    fila.imprimir_linha()
    print()

    print("=== Teste 4: após remover o primeiro ===")
    fila.pop()
    fila.imprimir()