from Tree import Tree
from Caminhao import Caminhao

class SistemaLogistico:
    def __init__(self):
        self.caminhoes = Tree()

    def adicionar_caminhao(self, caminhao):
        self.caminhoes.insert(caminhao)

    def inorder_traversal(self, node, caminhoes):
        if node:
            self.inorder_traversal(node.left, caminhoes)
            caminhoes.append(node.value)
            self.inorder_traversal(node.right, caminhoes)
        return caminhoes

    def imprimir_caminhoes(self, ordem='crescente'):
        caminhoes_ordenados = self.inorder_traversal(self.caminhoes.root, [])
        if ordem == 'decrescente':
            caminhoes_ordenados = caminhoes_ordenados[::-1]
        for caminhao in caminhoes_ordenados:
            print(caminhao)