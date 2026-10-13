class No:
    def __init__(self, valor):
        self.valor = valor
        self.prox = None


class Pilha:
    def __init__(self):
        self.topo = None

    def esta_vazia(self):
        return self.topo is None

    def push(self, valor):
        novo = No(valor)
        novo.prox = self.topo
        self.topo = novo

    def pop(self):
        if self.esta_vazia():
            print("Pilha vazia!")
            return None
        valor = self.topo.valor
        self.topo = self.topo.prox
        return valor

    def peek(self):
        return None if self.esta_vazia() else self.topo.valor

    def __str__(self):
        elementos = []
        atual = self.topo
        while atual:
            elementos.append(str(atual.valor))
            atual = atual.prox
        return "Topo -> " + " -> ".join(elementos) + " -> None" if elementos else "Pilha vazia"


# ---------- Função do Exercício 2 ----------
def inverter_sequencia():
    pilha = Pilha()
    n = int(input("Quantos números? "))

    for i in range(n):
        x = float(input(f"Número {i + 1}: "))
        pilha.push(x)

    print("\nOrdem inversa:")
    while not pilha.esta_vazia():
        print(pilha.pop(), end=" ")
    print()


# ---------- Teste ----------
if __name__ == "__main__":
    inverter_sequencia()