from LinkedList import LinkedList


class Caminhao:
    def __init__(self, capacidade_peso, capacidade_volume):
        self.capacidade_peso = capacidade_peso
        self.capacidade_volume = capacidade_volume
        self.cargas = []

    def __lt__(self, other):
        return self.capacidade_peso < other.capacidade_peso

    def adicionar_carga(self, carga):
        self.cargas.append(carga)

    def __str__(self):
        cargas_str = ', '.join(str(carga) for carga in self.cargas)
        return f'Caminhao(capacidade_peso={self.capacidade_peso}, capacidade_volume={self.capacidade_volume}, cargas=[{cargas_str}])'