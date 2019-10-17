import xlrd # pip install xlrd
from arrays import Array3D

def main():
    a3 = Array3D(39,38,19)
    for anio in range(1985,2019,1):
        ruta = './Precipitacion/'+str(anio)+'Precip.xls'
        #print(ruta)
        archivo = xlrd.open_workbook(filename=ruta)
        hoja = archivo.sheet_by_index(0)
        for r in range(1,33,1):
            for c in range(0,14,1):
                #print(hoja.cell_value(r,c) , end='')
                #print(anio , r , c)
                a3.set_item(anio-1985,r-1,c,hoja.cell_value(r , c ))
    #a3.to_string()
    a = int(input("Año(1985 - 2019):"))
    e = int(input("Edo (1-32:"))
    m = int(input("Mes(1-12):"))
    print(f" {a3.get_item(a-1985,e,m)} ")
main()
