

class Fila:

    # Método executado quando a fila é criada #
    def __init__(self):

        # Lista vazia #
        self.fila = []

    # Inserir pessoa na fila #
    def inserir(self, valor):

        # Adiciona no final da fila #
        self.fila.append(valor)

    # Atender pessoa da fila #
    def remover(self):

        # Verifica se a fila tem elementos #
        if len(self.fila) > 0:

            # Remove o primeiro elemento #
            return self.fila.pop(0)

        else:

            # Fila vazia #
            return "A fila está vazia."

    # Mostrar fila #
    def mostrar(self):

        # Retorna os elementos da fila #
        return self.fila