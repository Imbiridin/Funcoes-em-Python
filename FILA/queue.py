from fila import Fila

f = Fila()
print(f)

for i in range(4):
    f.insere(i)
    f.remove()
    print(f)
    
