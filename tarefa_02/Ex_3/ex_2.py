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

    # ---------- NOVO: busca por posição ----------
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

    def __str__(self):
        elementos = []
        atual = self.inicio
        while atual:
            elementos.append(str(atual.valor))
            atual = atual.prox
        return "Início -> " + " -> ".join(elementos) + " -> None" if elementos else "Fila vazia"

    def __len__(self):
        return self.tamanho
    

if __name__ == "__main__":
    fila = Fila()

    # Preenche a fila com alguns valores de exemplo
    for v in [10, 20, 30, 40, 50]:
        fila.push(v)

    print("Fila atual:", fila)
    print()

    # Loop de buscas
    while True:
        entrada = input("Digite um valor inteiro para buscar (ou 's' para sair): ")

        if entrada.lower() == 's':
            break

        try:
            valor = int(entrada)
        except ValueError:
            print("Entrada inválida! Digite um número inteiro.\n")
            continue

        pos = fila.buscar(valor)

        if pos == -1:
            print(f"Valor {valor} NÃO encontrado na fila.\n")
        else:
            print(f"Valor {valor} encontrado na posição {pos}.\n")

    print("Encerrando. Fila final:", fila)