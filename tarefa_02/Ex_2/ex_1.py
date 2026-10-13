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


# ---------- Função do exercício ----------
def maior_elemento(pilha):
    if pilha.esta_vazia():
        print("Pilha vazia!")
        return None

    aux = Pilha()
    maior = pilha.pop()
    aux.push(maior)

    while not pilha.esta_vazia():
        v = pilha.pop()
        if v > maior:
            maior = v
        aux.push(v)

    # Restaura a pilha original
    while not aux.esta_vazia():
        pilha.push(aux.pop())

    return maior


# ---------- Teste ----------
if __name__ == "__main__":
    p = Pilha()
    for v in [5, 12, 3, 8]:
        p.push(v)

    print("Pilha:", p)
    print("Maior elemento:", maior_elemento(p))
    print("Pilha após consulta:", p)  # preservada