from Tree import Tree
from Caminhao import Caminhao

class SistemaLogistico:
    def __init__(self):
        self.caminhoes = []

    def adicionar_caminhao(self, caminhao):
        self.caminhoes.append(caminhao)

    def quicksort(self, caminhoes, chave):
        if len(caminhoes) < 2:
            return caminhoes
        else:
            pivot = caminhoes[0]
            less = [i for i in caminhoes[1:] if getattr(i, chave) <= getattr(pivot, chave)]
            greater = [i for i in caminhoes[1:] if getattr(i, chave) > getattr(pivot, chave)]
            return self.quicksort(less, chave) + [pivot] + self.quicksort(greater, chave)

    def imprimir_caminhoes(self, ordem='crescente'):
        caminhoes_ordenados = self.quicksort(self.caminhoes, chave='peso')
        if ordem == 'decrescente':
            caminhoes_ordenados = caminhoes_ordenados[::-1]
        for caminhao in caminhoes_ordenados:
            print(caminhao)