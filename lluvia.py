import xlrd # 
from Array import Array3D

def main():
    pro=0
   
    promedio =0
    
    a3= Array3D(14,34,35)
    for anio in range(1985,2020,1):
        ruta='./precipitacion/'+str(anio)+ 'Precip.xls'
        #print(ruta)
        archivo= xlrd.open_workbook(filename=ruta)
        hoja= archivo.sheet_by_index(0)
        for r in range (1,34,1):
            for c in range (0,14,1):
               # print(hoja.cell_value(r,c), end='')
                #print(anio,r ,c)
                a3.set_item(anio-1985,r-1,c,hoja.cell_value(r,c))
    a=int(input("Seleccione un año:(1985-2019)"))
    e=int(input("Seleccione un Estado: 1-32: "))
    m=int(input("Seleccione un Mes:(1-12): "))
    print("__________________________________________")
    print(f"En el estado de ", hoja.cell_value(e-34,0)+
          f" llovió un promedio de {a3.get_item(a-1985,e,m)} centimetros cubicos"+
          f" en el mes de ", hoja.cell_value(1,m-14)+
          f" de {a}")
    print("__________________________________________")
    for anio in range(1985,2020,1):
        #print(a3.get_item(anio-1985,e,m))
        pro= (pro + a3.get_item(anio-1985,e,m))
        promedio = pro/34
    print(f"el promedio de las lluvias en es mes de ", hoja.cell_value(1,m-14)+ f" de todos los años es de",promedio)
    print("__________________________________________")
    for anio in range(1985,2019,1):
         for r in range(1,13,1):
           # print(a3.get_item(anio-1985,e,r), type(a3.get_item(anio-1985,e,r)))
            pro=pro + (a3.get_item(anio-1985,e,r))
            promedio = (pro/12)/34
    print("El promedio en el estado de " , hoja.cell_value(e-34,0)+
          " En todos los meses de todos los años es de: ", promedio)
    for anio in range(1985,2019,1):
        for r in range(1,13,1):
            
            for c in range(1,34,1):
                #print(a3.get_item(anio-1985,c,r), type(a3.get_item(anio-1985,e,r)))
                pro= pro + (a3.get_item(anio-1985,e,r))
                promedio = ((pro/12)/34)/32
    print("____________________________")
    print("El promedio de lluvias de Todos los estados, todos los meses para  todos los años es de :" ,promedio)
                
main()


