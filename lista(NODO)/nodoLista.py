class nodoLista:
    def __init__(self, nodo, proximo_nodo=None):
        self.nodo = nodo
        self.proximo_nodo = proximo_nodo

    def __repr__(self):
        return "%s -> %s" % (self.nodo, self.proximo_nodo)

class ListaEncadeada:
    def __init__(self):
        self.cabeca = cabeca = None

    def __repr__(self):
        return '[' + str(self.cabeca) + ']'

def insere_inicio(lista, novo_dado):
    #criar o nodo
    novo_nodo = nodoLista(novo_dado)
    
    #Novo nodoaponta para o nodo da cabeca
    novo_nodo.proximo_nodo = lista.cabeca
    
    #Cabeca aponta para quem chegou
    lista.cabeca = novo_nodo
          
    
#Saída dos nodos
if __name__ == '__main__':
    print("Nodo 1 nasceu")
    nodo_1 = nodoLista("Marcos")
    print(nodo_1)

    print("Nodo 2 nasceu")
    nodo_2 = nodoLista("João")
    print(nodo_2)
    
    print("Nodo 3 nasceu")
    nodo_3 = nodoLista("Denis")
    print(nodo_3)

    print("Nodo 1 ponta para o nodo 2")
    nodo_1.proximo_nodo = nodo_2
    
    print("Nodo 2 ponta para o nodo 3")
    nodo_2.proximo_nodo = nodo_3

    print("Lista criada")
    lista = ListaEncadeada()
    lista.cabeca = nodo_1

    print(lista)
    
    insere_inicio(lista,novo_dado="Viviane")
        
    print(lista)