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
        if self.esta_vazia():
            return None
        return self.topo.valor

    def __str__(self):
        elementos = []
        atual = self.topo
        while atual:
            elementos.append(str(atual.valor))
            atual = atual.prox
        return "Topo -> " + " -> ".join(elementos) + " -> None" if elementos else "Pilha vazia"


def TPilha(vetor):
    if len(vetor) != 15:
        print("Erro: o vetor deve ter exatamente 15 elementos.")
        return

    pilha = Pilha()

    print("Processando os elementos:")
    for i, num in enumerate(vetor):
        if num % 2 == 0:
            pilha.push(num)
            print(f"[{i:2}] {num:4} é PAR   -> empilha  | {pilha}")
        else:
            removido = pilha.pop()
            if removido is None:
                print(f"[{i:2}] {num:4} é ÍMPAR -> pilha vazia, nada a remover")
            else:
                print(f"[{i:2}] {num:4} é ÍMPAR -> desempilha {removido} | {pilha}")

    print("\nEsvaziando a pilha:")
    if pilha.esta_vazia():
        print("Pilha vazia — nenhum elemento a imprimir.")
    else:
        while not pilha.esta_vazia():
            print(pilha.pop(), end=" ")
        print()


# ---------------- Teste ----------------
if __name__ == "__main__":
    vetor = [10, 3, 4, 7, 8, 1, 6, 5, 12, 9, 2, 11, 14, 13, 16]
    TPilha(vetor)