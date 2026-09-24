pilhas = [1,1,2,3,5]
print("pilha",pilhas)

sahlip = []
print("pilha invertida",sahlip)

pilhas.append(8)
print("Inserindo outro elemento: ",pilhas)

pilhas.pop()
print("Removendo um elemento: ", pilhas)

pilhas.pop()
print("Removendo outro elemento: ", pilhas)

print("-"*50)

palavra = "PYTHON"
pilha = []

for i in palavra:
    pilha.append(i)

print(pilha)

sahlip = []

while pilha:
    sahlip += pilha.pop()
    
print(sahlip)
print("="*50)

palindromo = 'arara'

pilha = []

for i in palindromo:
    pilha.append(i)
  
invertido = ""
  
while pilha:
    invertido += pilha.pop()
    
if palindromo == invertido:
    print("É palindromo")
else:
    print("Não é palindormo")
    
print("/"*50)

historico = []

pag_atual = "google.com"

def acessar(nova_pagina):
    global pag_atual
    historico.append(pag_atual)
    pag_atual = nova_pagina
    
def voltar():
    global pag_atual
    if historico:
        pag_atual = historico.pop()
    
#Main

acessar("youtube.com")
acessar("senac.com")
acessar("github.com")

print(pag_atual)

voltar()
print(pag_atual)