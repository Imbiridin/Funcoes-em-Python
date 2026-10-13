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


# ---------- Funções do Exercício 4 ----------
def contem_placa(rua, placa):
    """Verifica se a placa existe sem destruir a pilha."""
    aux = Pilha()
    achou = False

    while not rua.esta_vazia():
        v = rua.pop()
        if v == placa:
            achou = True
        aux.push(v)

    while not aux.esta_vazia():
        rua.push(aux.pop())

    return achou


def verificar_carro(rua, placa):
    if not contem_placa(rua, placa):
        print(f"O carro de placa {placa} NÃO está estacionado.")
        return

    print(f"Carros que devem ser retirados para liberar a placa {placa}:")
    aux = Pilha()

    while not rua.esta_vazia():
        v = rua.pop()
        if v == placa:
            print(f"-> Placa {v} (o próprio carro) sai.")
            break
        else:
            print(f"-> Retirar placa {v}")
            aux.push(v)

    # Devolve os carros removidos à rua (ordem original)
    while not aux.esta_vazia():
        rua.push(aux.pop())


# ---------- Teste ----------
if __name__ == "__main__":
    rua = Pilha()

    # Ordem de entrada: 111, 222, 333, 444
    for placa in [111, 222, 333, 444]:
        rua.push(placa)

    print("Rua (topo = saída):", rua, "\n")
    verificar_carro(rua, 222)
    print("\nRua após a operação:", rua)