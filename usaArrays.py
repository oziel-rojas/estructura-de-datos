from arrays import Array , Array2D

def main():
    arr = Array(7)
    arr.to_string()
    print(f"El arr es de {arr.length()} elementos")
    arr.set_item( 3 , 11 )
    arr.to_string()
    print(f"Elem. en la pos 3 es: { arr.get_item(3) }")
    arr.clearing( 55 )
    arr.to_string()
    arr2d = Array2D(4,4)
    arr2d.to_string()

main()
