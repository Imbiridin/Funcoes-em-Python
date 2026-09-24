class Nodo:
    
    def __init__(self,dado=0, nodo_anterior=None):
        self.dado = dado
        self.nodo_anterior = nodo_anterior
    
    def __repr__(self):
        return '%s -> %s' % (self.dado, self.anterior)
    

class Pilha:
    
    def __init__(self):
        self.topo = None
        
    def __repr__(self):
        return "[" + str(self.topo) + "]"
    
    def insere(self, novo_dado):
        
        novo_nodo = Nodo(novo_dado)
        
        novo_nodo.anterior = self.topo
        
    def remove(self):
        
        assert self.topo, "Impossível remover valor da pilha vazia."
        
        self.topo = self.topo.anterior
        

pilha = Pilha()
print("Pilha vazia: ", pilha)

for i in range(5):
    pilha.insere(i)
    print("Insere o valor {0} no topo da pilha: {1}".format(i,pilha))
    
while pilha.topo != None:
    pilha.remove()
    print("Removendo elemento que está no topo da pilha: ", pilha)
        