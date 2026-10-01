class Nodo:
    """Esta classe representa um nodo de um estrutura duplamente encadeada"""
    
    def __init__(self,dado=0, proximo_nodo=None):
        self.dado = dado
        self.proximo = proximo_nodo
        
    def __repr__(self):
        return '%s -> %s' % (self.dado, self.proximo)
    
class Fila:
    """Esta classe representa uma fila usando uma estrutura encadeada"""
    
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
        
    def __repr__(self):
        return "(" + str(self.primeiro) + ")"
    
    def insere(self,novo_nodo):
        """Insere um elemento no final da lista"""
        
        #Cria um novo nodo com o dado a ser armazenado
        novo_nodo = Nodo(novo_nodo)

        #Insere em uma dila vazia
        if self.primeiro == None:
            self.primeiro = novo_nodo
            self.ultimo = novo_nodo
        else:
            #Faz com que o novo nodo seja o último da fila
            self.ultimo.proximo = novo_nodo
            
            #Faz com que o último da fila referencie o novo nodo
            self.ultimo =novo_nodo

    def remove(self):
        """Remove o último elemento da lista"""
            
        assert self.primeiro != None, "Impossível remover elemento de fila vazia"
            
        self.primeiro = self.primeiro.proximo
            
        if self.primeiro == None:
            self.ultimo
            
if __name__ == "__main__":
    pass