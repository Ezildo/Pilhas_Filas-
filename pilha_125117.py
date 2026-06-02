
# Criamos uma classe chamada Pilha #
class Pilha:

    # Método executado quando a Pilha é criada #
    def __init__(self):

        # Lista vazia onde os dados serão guardados #
        self.pilha = []

    # Função para adicionar elementos #
    def inserir(self, valor):

        # Adiciona o valor no final da lista #
        self.pilha.append(valor)

    # Função para remover elementos #
    def remover(self):

        # Verifica se existe algum elemento #
        if len(self.pilha) > 0:

            # Remove o último elemento inserido #
            return self.pilha.pop()

        else:

            # Caso a pilha esteja vazia #
            return "A pilha está vazia."

    # Função para mostrar a pilha #
    def mostrar(self):

        # Devolve todos os elementos #
        return self.pilha