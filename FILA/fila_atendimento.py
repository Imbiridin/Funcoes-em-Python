class Atendimento:
    
    def __init__(self,dado = 0, proximo_nodo=None):
        self.dado = dado
        self.proximo = proximo_nodo
        
    def __repr__(self):
        return '%s -> %s' % (self.dado, self.proximo)
    
class Fila:
    
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
        
    def __repr__(self):
        return str(self.primeiro)
    
    def insere(self, novo_nodo):
        
        novo_nodo = Atendimento(novo_nodo)
        
        if self.primeiro == None:
            self.primeiro = novo_nodo
            self.ultimo = novo_nodo
        else:
            self.ultimo.proximo = novo_nodo
            self.ultimo = novo_nodo
    
    def remove(self):
        assert self.primeiro != None , "Impossível remover elemento de fila vazia"
        
        self.primeiro = self.primeiro.proximo
        
        if self.primeiro == None:
            self.ultimo

if __name__ == "__main__":
    pass