class Carga:
    def __init__(self, peso, volume):
        self.peso = peso
        self.volume = volume

    def __str__(self):
        return f'Carga(peso={self.peso}, volume={self.volume})'
