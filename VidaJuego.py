from arrays import Array2D

class VidaJuego:
    
    def __init__(self, rows, cols):
        self.__arr=Array2D(rows, cols)

    def get_rows(self):
        return self.___arr.get_num_rows()

    def get_cols(self):
        return self.___arr.get_num_cols()

    def configure(self,coordList):
         
        #cooordlist es una lista de celualas vivas con la forma
        #[1,2],[2,1],[2,2],[2,3]
    
        self.__arr.clearing( 0 )
        for cell in coordList :
            self.__arr.set_item(cell[0],cell[1],1)
            
    def clear_cell(self, row, col):
        self.__arr.set_item(row, col,0)

    def set_cell(self, row, col):
        self.__arr.set_item(row, col,1)

    def is_live_cell(self,row,col):
        return self.__arr.get_item(row,col)==1

    def get_num_live_neighbors(self, row, col):
        vivos=0
        for r in range(row-1,row + 2,1):
            for c in range(col-1, col+2,1):
                if r == row and c == col:
                    pass
                elif self.__arr.get_item(r,c)==1:
                    vivos +=1
        return vivos
    def to_string(self):
        self.__arr.to_string()

def main():
    juego=VidaJuego(5,5)
    generaciones=4
    poblacion_inicial=[[1,2],[2,1],[2,2],[2,3]]
    juego.configure(poblacion_inicial)
    juego.to_string()
    print(f"la celula 1,2 tiene {juego.get_num_live_neighbors(1,2)} vecinos vivos")


main()
    
