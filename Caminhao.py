from LinkedList import LinkedList
from barcode import EAN13
from barcode.writer import ImageWriter

class Caminhao:
    def __init__(self, id, capacidade_peso, capacidade_volume, peso):
        self.id = id
        self.peso = peso
        self.capacidade_peso = capacidade_peso
        self.capacidade_volume = capacidade_volume
        self.cargas = []

    def __lt__(self, other):
        return self.capacidade_peso < other.capacidade_peso

    def adicionar_carga(self, carga):
        self.cargas.append(carga)

    def gerar_codigo_barras(self):
        id_str = str(self.id).zfill(12)
        codigo_barras = EAN13(id_str, writer=ImageWriter())
        codigo_barras.save(f'caminhao_{self.id}')
        print(f"Código de barras para o caminhão {self.id} foi gerado e salvo como 'caminhao_{self.id}.png'")

    def __str__(self):
        cargas_str = ', '.join(str(carga) for carga in self.cargas)
        return f"\nCaminhao {self.id}\n\tCapacidade de Peso={self.capacidade_peso},\n\tCapacidade de Volume={self.capacidade_volume},\n\t{cargas_str}\n\t\n"
    
    def __repr__(self):
        return self.__str__()