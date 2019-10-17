#metodeo de ordenamiento burbuja
def burbuja( lista ):
    print(f"Original: {lista}")
    for tope in range(len(lista)-1,0,-1):
        for pivote in range(tope):
            if lista[pivote]>lista[pivote+1]:
                lista[pivote] , lista[pivote+1] = lista[pivote+1],lista[pivote]
    return lista

#metodo de ordenamiento por seleccon
def seleccion(lista):
    print(f"Original: {lista}")
    for pivote in range (0,len(lista)-1,1):
        menor=pivote
        for index in range(pivote,len(lista),1):
            if lista[index] < lista[menor]:
                menor=index
        lista[pivote],lista[menor]=lista[menor],lista[pivote]
    return lista

#metodo de interseccion
def interseccion(lista):
    print(f"Original: {lista}")
    for pivote in range(1,len(lista),1):
        for index in range(pivote+1):
            if lista[pivote] < lista[index]:
                tmp=lista[index]
                lista[index] = lista[pivote]
                #recorrer a la derecha
                for i in range(index-1,pivote+1,1):
                    tmp2=lista[i]
                    lista[i]=tmp
                    tmp=tmp2
        print(lista)
    return lista


def main():
    l = [3,8,9,5,0]
    print(burbuja(l))
    numeros=[3,5,99,0,22,31,4]
    print(seleccion(numeros))
    print(interseccion(numeros))
    nombre=['carlos','enrique','zoila','alberto','benita','diana']
    print(seleccion(nombre))
main()
