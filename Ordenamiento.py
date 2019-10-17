def burbuja(n):
    lista = []
    for x in range(0, n,1):
        lista.insert(x , int(input(f"Ingresa el {x+1} valor")))
    

    for tope in range(len(lista)-1,0,-1):   #Es para decir hasta que elemto va a comparar
        for pivote in range(tope):
            if lista[pivote] > lista[pivote+1]:
                """
                para ahorrar lineas
                lista[pivote] , lista[pivote+1] = lista[pivote+1] , lista[pivote]
                """
                aux = lista[pivote]
                lista[pivote] = lista[pivote+1]
                lista[pivote+1] = aux
    return lista
def seleccion(lista):
    lista = []
    for x in range(0, n,1):
        lista.insert(x , int(input(f"Ingresa el {x+1} valor")))

    for pivote in range(0,len)
    
    
def main():
    n = int(input("¿Cuantos numeros ingresaras?"))
    print(burbuja(n))
main()
