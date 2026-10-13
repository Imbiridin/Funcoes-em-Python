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
    
class Navegador:
    def __init__(self):
        self.historico = Pilha()   # páginas para voltar
        self.futuro = Pilha()      # páginas para avançar
        self.atual = None

    def visitar(self, url):
        # Guarda a página atual no histórico
        if self.atual is not None:
            self.historico.push(self.atual)

        self.atual = url
        self.futuro = Pilha()      # nova visita descarta o "avançar"
        print(f"🌐 Visitando: {url}")

    def voltar(self):
        if self.historico.esta_vazia():
            print("⚠ Não há páginas anteriores.")
            return

        self.futuro.push(self.atual)       # atual vai para o futuro
        self.atual = self.historico.pop()  # anterior vira atual
        print(f"⬅ Voltando para: {self.atual}")

    def avancar(self):
        if self.futuro.esta_vazia():
            print("⚠ Não há páginas à frente.")
            return

        self.historico.push(self.atual)    # atual vai para o histórico
        self.atual = self.futuro.pop()
        print(f"➡ Avançando para: {self.atual}")
        
if __name__ == "__main__":
    nav = Navegador()

    nav.visitar("google.com")
    nav.visitar("youtube.com")
    nav.visitar("github.com")

    nav.voltar()      # youtube.com
    nav.voltar()      # google.com

    nav.avancar()     # youtube.com

    nav.visitar("python.org")   # descarta o "futuro"
    nav.voltar()      # youtube.com
    nav.voltar()      # google.com
    nav.voltar()      # ⚠ não há mais