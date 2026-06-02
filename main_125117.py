# Importa a classe Pilha #
from pilha import Pilha

# Importa a classe Fila #
from fila import Fila

# Cria uma pilha #
pilha = Pilha()

# Cria uma fila #
fila = Fila()


# TESTE DA PILHA #

print(" PILHA ")

# Inserir livros #
pilha.inserir("Livro 1")
pilha.inserir("Livro 2")
pilha.inserir("Livro 3")
pilha.inserir("Livro 4")
pilha.inserir("Livro 5")
pilha.inserir("Livro 6")

# Mostrar pilha #
print("Pilha atual:")
print(pilha.mostrar())

# Remover último livro #
print("Livro removido:")
print(pilha.remover())

# Mostrar novamente #
print("Pilha depois da remoção:")
print(pilha.mostrar())

# TESTE DA FILA #


print(" FILA\n ")

# Inserir pessoas #
fila.inserir("Adelino")
fila.inserir("Baptista")
fila.inserir("Kawe")
fila.inserir("Ezildo")
fila.inserir("Daniela")
fila.inserir("Suviclânia")

# Mostrar fila #
print("Fila atual:")
print(fila.mostrar())

# Atender pessoa #
print("Pessoa atendida:")
print(fila.remover())

# Mostrar fila novamente #
print("Fila depois do atendimento:")
print(fila.mostrar())