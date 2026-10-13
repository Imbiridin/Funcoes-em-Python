class Processo:
    """Representa um processo em execução."""
    def __init__(self, pid, nome, status, cpu, memoria):
        self.pid = pid
        self.nome = nome
        self.status = status
        self.cpu = cpu
        self.memoria = memoria
        self.prox = None

    def __str__(self):
        return f"{self.pid:>6} | {self.nome:<20} | {self.status:<14} | {self.cpu:>5}% | {self.memoria:>7} MB"


class GerenciadorTarefas:
    """Lista encadeada que simula o Gerenciador de Tarefas do Windows."""

    def __init__(self):
        self.inicio = None
        self.tamanho = 0

    def esta_vazia(self):
        return self.inicio is None

    # ---------- Adicionar processo ----------
    def adicionar(self, pid, nome, status="Em execução", cpu=0, memoria=0):
        novo = Processo(pid, nome, status, cpu, memoria)

        if self.esta_vazia():
            self.inicio = novo
        else:
            atual = self.inicio
            while atual.prox is not None:
                atual = atual.prox
            atual.prox = novo

        self.tamanho += 1
        print(f"✔ Processo '{nome}' (PID {pid}) iniciado.")

    # ---------- Encerrar processo pelo PID ----------
    def encerrar(self, pid):
        if self.esta_vazia():
            print("Nenhum processo em execução.")
            return

        # Caso especial: remover o primeiro
        if self.inicio.pid == pid:
            removido = self.inicio
            self.inicio = self.inicio.prox
            self.tamanho -= 1
            print(f"✘ Processo '{removido.nome}' (PID {pid}) encerrado.")
            return

        # Remover no meio/fim
        anterior = self.inicio
        atual = self.inicio.prox
        while atual is not None:
            if atual.pid == pid:
                anterior.prox = atual.prox
                self.tamanho -= 1
                print(f"✘ Processo '{atual.nome}' (PID {pid}) encerrado.")
                return
            anterior = atual
            atual = atual.prox

        print(f"⚠ Nenhum processo com PID {pid} foi encontrado.")

    # ---------- Exibir todos os processos ----------
    def exibir(self):
        if self.esta_vazia():
            print("Nenhum processo em execução.")
            return

        print("\n" + "=" * 70)
        print(f"{'PID':>6} | {'NOME':<20} | {'STATUS':<14} | {'CPU':>6} | {'MEMÓRIA':>10}")
        print("-" * 70)

        atual = self.inicio
        while atual is not None:
            print(atual)
            atual = atual.prox

        print("=" * 70)
        print(f"Total de processos: {self.tamanho}\n")

    # ---------- Buscar processo por nome ----------
    def buscar(self, nome):
        atual = self.inicio
        pos = 1
        while atual is not None:
            if atual.nome.lower() == nome.lower():
                return pos, atual
            atual = atual.prox
            pos += 1
        return -1, None


# ---------------- Programa principal ----------------
if __name__ == "__main__":
    gerenciador = GerenciadorTarefas()

    # Simulando a abertura de programas
    gerenciador.adicionar(1024, "chrome.exe",     cpu=12, memoria=850)
    gerenciador.adicionar(2048, "explorer.exe",   cpu=1,  memoria=45)
    gerenciador.adicionar(3072, "word.exe",       cpu=0,  memoria=120, status="Suspenso")
    gerenciador.adicionar(4096, "spotify.exe",    cpu=3,  memoria=210)
    gerenciador.adicionar(5120, "vscode.exe",     cpu=8,  memoria=430)
    gerenciador.adicionar(6144, "antivirus.exe",  cpu=0,  memoria=90,  status="Suspenso")

    # Exibe a "tela" do gerenciador
    gerenciador.exibir()

    # Simula fechar o Spotify
    gerenciador.encerrar(4096)
    gerenciador.exibir()

    # Simula fechar o Word (que estava suspenso)
    gerenciador.encerrar(3072)
    gerenciador.exibir()

    # Tentando fechar um processo que não existe
    gerenciador.encerrar(9999)

    # Busca por nome
    pos, proc = gerenciador.buscar("chrome.exe")
    if proc:
        print(f"\n🔎 Encontrado na posição {pos}: {proc}")