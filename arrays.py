#ADT Arreglo"
#Un adt que almacenavalores del mismo tipo,
#pero difernciados por un indiice
#ARREGLO DE UNA DIMENSION
class Array:
    def __init__(self,n):
        self.__n =n
        self.__arreglo=[]
        for i in range(0,n,1):
            self.__arreglo.append(0)
                
    def length(self):
        return self.__n
    
    def get_item(self,index):
        return self.__arreglo[index]
    
    def set_item(self,index,value):
        self.__arreglo[index]=value
        
    def clearing(self, value):
        for i in range(0,self.__n,1):
            self.__arreglo[i]=value

    def to_string(self):
        print(f"Tamaño de arreglo = {self.__n}")
        print(self.__arreglo)

#ARREGLO DE DOS DIMENSIONES

class Array2D:
    def __init__(self,rows,cols):
        self.__rows = rows
        self.__cols = cols
        self.__arreglo = []
        for r in range(self.__rows):
            tmp=[]
            for c in range(self.__cols):
                tmp.append(0)
            self.__arreglo.append(tmp)
            
    def to_string(self):
        for ren in self.__arreglo:
            print(ren)
    def get_num_rows(self):
        return self.__rows
    def _num_cols(self):
        return self.__cols
    def set_item(self,rows,cols,value):
        self.__arreglo[rows][cols] = value
    def get_item(self,rows,cols):
            return self.__arreglo[rows][cols]
    def clearing(self,value):
        for i in range(self.__rows):
            for j in range (self.__cols):
                 self.__arreglo[i][j]=value
