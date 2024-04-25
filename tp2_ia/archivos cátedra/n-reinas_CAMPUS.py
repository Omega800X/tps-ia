""" Puzzle n-reinas. """
class NQueens:
    """ Genere todas las soluciones válidas para el puzzle de n reinas """
    def __init__(self, size):
        # Almacene el tamaño del puzzle (problema) y la cantidad de soluciones válidas
        self.size = size
        self.solutions = 0
        self.solve()

    def solve(self):
        """ Resuelve el puzzle de las n reinas e imprime el número de soluciones """
        positions = [-1] * self.size
        self.put_queen(positions, 0)
        print("Found", self.solutions, "solutions.")

    def put_queen(self, positions, target_row):
        
        """  
        Intente colocar una reina en target_row marcando todos los N casos posibles. 
        Si se encuentra un lugar válido, la función se llama a sí misma tratando de colocar
        una reina en la siguiente fila hasta que todas las N reinas se colocan en el tablero NxN. 
        """
        
        # Caso base (corte) todas las N filas están ocupadas
        if target_row == self.size:
            self.show_full_board(positions)
            # self.show_short_board(positions)
            self.solutions += 1
        else:
            # Para todas las posiciones de N columnas, intente colocar una reina
            for column in range(self.size):
                # Rechazar todas las posiciones inválidas
                if self.check_place(positions, target_row, column):
                    positions[target_row] = column
                    self.put_queen(positions, target_row + 1)


    def check_place(self, positions, ocuppied_rows, column):
        
        """ Compruebe si una posición determinada está siendo atacada 
        por alguna de las reinas colocadas anteriormente 
        (verifique las posiciones de la columna y la diagonal) """
        
        for i in range(ocuppied_rows):
            if positions[i] == column or \
                positions[i] - i == column - ocuppied_rows or \
                positions[i] + i == column + ocuppied_rows:

                return False
        return True

    def show_full_board(self, positions):
        """ Mostrar el tablero completo de NxN """
        for row in range(self.size):
            line = ""
            for column in range(self.size):
                if positions[row] == column:
                    line += "Q " 
                else:
                    line += ". "
            print(line)
        print("\n")

    def show_short_board(self, positions):
        
        """ Muestre las posiciones de las reinas en el tablero en forma comprimida, 
        cada número representa la posición de la columna ocupada en la fila correspondiente. """
        
        line = ""
        for i in range(self.size):
            line += str(positions[i]) +  " "
        print(line)

def main():
    """ Inicializa y resuelve el rompecabezas de n reinas """
    NQueens(4)

if __name__ == "__main__":
    # execute only if run as a script
    main()
