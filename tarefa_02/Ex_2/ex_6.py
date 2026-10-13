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


def TPilha2(N, P, vetor):
    print("Processando os elementos:\n")

    for i, num in enumerate(vetor):
        if num > 0:
            P.push(num)
            print(f"[{i:2}] {num:5} > 0  -> empilha em P | P: {P}")

        elif num < 0:
            N.push(num)
            print(f"[{i:2}] {num:5} < 0  -> empilha em N | N: {N}")

        else:  # num == 0
            removidoN = N.pop()
            removidoP = P.pop()

            msgN = f"desempilha {removidoN} de N" if removidoN is not None else "N vazia"
            msgP = f"desempilha {removidoP} de P" if removidoP is not None else "P vazia"
            print(f"[{i:2}] {num:5} == 0 -> {msgN}; {msgP}")

    print("\n--- Estado final ---")
    print("Pilha N:", N)
    print("Pilha P:", P)


# ---------------- Teste ----------------
if __name__ == "__main__":
    vetor = [5, -3, 8, 0, -7, 2, -1, 0, 4, -6, 9, 0, -2, 10, -8]

    N = Pilha()
    P = Pilha()

    TPilha2(N, P, vetor)