from Conexion import *
if __name__ == "__main__":
    print ("-----------------------------")
    print ("Menu de selecion")
    print ("Buscar producto")
    producto = input(str())
    print(f"Su producto es un.. {producto}")
    search(producto)
    print ("-----------------------------")