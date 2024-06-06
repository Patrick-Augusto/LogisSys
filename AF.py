from SistemaLogistico import SistemaLogistico
from Caminhao import Caminhao
from Carga import Carga

def main():
    sistema = SistemaLogistico()

    num_caminhoes = int(input("Digite o número de caminhões: "))
    
    for i in range(num_caminhoes):
        capacidade_peso = int(input(f"Digite a capacidade de peso do caminhão {i+1}: "))
        capacidade_volume = int(input(f"Digite a capacidade de volume do caminhão {i+1}: "))
        caminhao = Caminhao(capacidade_peso, capacidade_volume)

        peso_carga = int(input(f"Digite o peso da carga para o caminhão {i+1}: "))
        volume_carga = int(input(f"Digite o volume da carga para o caminhão {i+1}: "))
        carga = Carga(peso_carga, volume_carga)

        caminhao.adicionar_carga(carga)
        sistema.adicionar_caminhao(caminhao)

    sistema.imprimir_caminhoes()

if __name__ == "__main__":
    main()