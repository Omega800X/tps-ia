class Marco:
    def __init__(self, tamanio):
        self.tamanio = tamanio
        self.marco = [
            self.crear_fila_borde(tamanio) if (i == 0) or (i == tamanio - 1) 
            else self.crear_fila_centro(tamanio) 
            for i in range(0, tamanio)
        ]

    def crear_fila_borde(self, longitud):
        return [1 for i in range(0, longitud)]

    def crear_fila_centro(self, longitud):
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
                    x.cambiar_valor(fila, columna, 1)
                if columna == (self.obtener_tamanio() - fila - 1):
                    x.cambiar_valor(fila, columna, 1)

    def cambiar_valor(self, x, y, valor):
        self.marco[x][y] = valor

    def obtener_tamanio(self):
        return self.tamanio

    def imprimir(self):
        for i in self.marco:
            print(i)



x = Marco(10)
print("--------------------Matriz Original--------------------")
x.imprimir()
x.llenar_diagonales_principales()
print("--------------------Matriz con Diagonales Principales en 1--------------------")
x.imprimir()
