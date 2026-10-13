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


# ---------- Função do Exercício 3 ----------
def pilhas_iguais(p1, p2):
    aux1 = Pilha()
    aux2 = Pilha()
    iguais = True

    while not p1.esta_vazia() and not p2.esta_vazia():
        v1 = p1.pop()
        v2 = p2.pop()
        if v1 != v2:
            iguais = False
        aux1.push(v1)
        aux2.push(v2)

    # Se uma das pilhas ainda tem elementos, são diferentes
    if not p1.esta_vazia() or not p2.esta_vazia():
        iguais = False

    # Restaura as pilhas originais
    while not aux1.esta_vazia():
        p1.push(aux1.pop())
    while not aux2.esta_vazia():
        p2.push(aux2.pop())

    return iguais


# ---------- Teste ----------
if __name__ == "__main__":
    a = Pilha()
    for v in [1, 2, 3]:
        a.push(v)

    b = Pilha()
    for v in [1, 2, 3]:
        b.push(v)

    c = Pilha()
    for v in [1, 2, 4]:
        c.push(v)

    print("a == b ?", pilhas_iguais(a, b))  # True
    print("a == c ?", pilhas_iguais(a, c))  # False
    print("a:", a)  # preservada
    print("b:", b)  # preservada
    print("c:", c)  # preservada