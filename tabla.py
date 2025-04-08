class Tabla:
    def __init__(self,numero):
        self.numero = numero
        
    def mostrarNormal(self):
        print(f'Tabla de {self.numero}(normal): ')
        for i in range(1,11):
            print(f'{self.numero} x {i}')
            
    def mostrarInvertida(self):
        print(f'Tabla del {self.numero}(invertida): ')
        for i in range(10, 0, -1):
            print(f'{self.numero} X {i} = {self.numero * i}')
##Clase
if __name__ == "__main__":
    num_usuario = int(input("Introduce un Numero para ver la tabla: "))
    num_tabla = Tabla(num_usuario)
    num_tabla.mostrarNormal()
    num_tabla.mostrarInvertida()