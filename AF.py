from SistemaLogistico import SistemaLogistico
from Caminhao import Caminhao
from Carga import Carga

def main():
    sistema = SistemaLogistico()

    num_caminhoes = int(input("Digite o número de caminhões: "))
    
    for i in range(num_caminhoes):
        capacidade_peso = int(input(f"Digite a capacidade de peso do caminhão {i+1}: "))
        capacidade_volume = int(input(f"Digite a capacidade de volume do caminhão {i+1}: "))
        peso = int(input(f"Digite o peso do caminhão {i+1}: "))  
        caminhao = Caminhao(id=i+1, capacidade_peso=capacidade_peso, capacidade_volume=capacidade_volume, peso=peso)  
 

        while True:
            peso_carga = int(input(f"Digite o peso da carga para o caminhão {i+1}: "))
            volume_carga = int(input(f"Digite o volume da carga para o caminhão {i+1}: "))
            if peso_carga > capacidade_peso or volume_carga > capacidade_volume:
                print("O peso e o volume da carga não podem ser maiores que o peso e o volume do caminhão. Por favor, digite novamente.")
            else:
                break

        carga = Carga(peso_carga, volume_carga)

        caminhao.adicionar_carga(carga)
        caminhao.gerar_codigo_barras()
        sistema.adicionar_caminhao(caminhao)
     

    ordem = input("Você quer a ordem crescente ou decrescente? ")
    sistema.imprimir_caminhoes(ordem=ordem)

if __name__ == "__main__":
    main()