class Marco:
    def __init__(self, tamanio):
        self.__marco = [
            self.__crear_fila_borde(tamanio) if (i == 0) or (i == tamanio - 1) 
            else self.__crear_fila_centro(tamanio) 
            for i in range(0, tamanio)
        ]

    def __crear_fila_borde(self, longitud):
        return [1 for i in range(0, longitud)]

    def __crear_fila_centro(self, longitud):
        return [
            1 if (i == 0) or (i == longitud - 1) 
            else 0 
            for i in range(0, longitud)
        ]
    
    def llenar_diagonales_principales(self):
        if self.obtener_tamanio() <= 2:
            return
        
        for fila in range(1, self.obtener_tamanio() - 1):
            for columna in range(1, self.obtener_tamanio() - 1):
                if fila == columna:
                    self.cambiar_valor(fila, columna, 1)
                if columna == (self.obtener_tamanio() - fila - 1):
                    self.cambiar_valor(fila, columna, 1)

    def cambiar_valor(self, x, y, valor):
        self.__marco[x][y] = valor

    def obtener_tamanio(self):
        return len(self.__marco)

    def imprimir(self):
        for i in self.__marco:
            print(i)



marco = Marco(10)
print("--------------------Matriz Original--------------------")
marco.imprimir()
marco.llenar_diagonales_principales()
print("--------------------Matriz con Diagonales Principales en 1--------------------")
marco.imprimir()
