from Tree import Tree
from Caminhao import Caminhao

class SistemaLogistico:
    def __init__(self):
        self.caminhoes = []

    def adicionar_caminhao(self, caminhao):
        self.caminhoes.append(caminhao)

    def imprimir_caminhoes(self):
        for caminhao in self.caminhoes:
            print(caminhao)

