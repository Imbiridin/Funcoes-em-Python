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
    
    
def inverter_string(texto):
    pilha = Pilha()

    # 1. Empilha todos os caracteres
    for c in texto:
        pilha.push(c)

    # 2. Desempilha formando a string invertida
    invertida = ""
    while not pilha.esta_vazia():
        invertida += pilha.pop()

    return invertida


if __name__ == "__main__":
    palavras = ["Python", "abc", "Estrutura", "a", ""]

    for p in palavras:
        print(f"'{p}' → '{inverter_string(p)}'")