import sqlite3 as sql

def createBase():
    conx = sql.connect("Productos.db")
    conx.commit()
    conx.close()

def createTable():
    conx = sql.connect("Productos.db")
    cursor = conx.cursor()
    cursor.execute(
        """CREATE TABLE Producto (
           Nombre text,
           Stock integer,
           Valor float
        ) """
        
    )
    conx.commit()
    conx.close()

def inserRow(Nombre, Stock, Valor):
    conx = sql.connect("Productos.db")
    cursor = conx.cursor()
    instruccion = f"INSERT INTO Producto Values('{Nombre}', {Stock}, {Valor})" 
    cursor.execute(instruccion)
    conx.commit()
    conx.close()

def readRows():
    conx = sql.connect("Productos.db")
    cursor = conx.cursor()
    instruccion = f"SELECT * FROM Producto"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conx.commit()
    conx.close()
    print(datos)

def insertRows(productoList):
    conx = sql.connect("Productos.db")
    cursor = conx.cursor()
    instruccion = f"INSERT INTO Producto VALUES (?, ?, ?)"
    cursor.executemany(instruccion, productoList)
    conx.commit()
    conx.close()

def readOrdered(field):
    conx = sql.connect("Productos.db")
    cursor = conx.cursor()
    instruccion = f"SELECT * FROM Producto ORDER BY {field} DESC"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conx.commit()
    conx.close()
    print(datos)

def search(field):
    conx = sql.connect("Productos.db")
    cursor = conx.cursor()
    instruccion = f"SELECT * FROM Producto WHERE Nombre like '{field}'"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conx.commit()
    conx.close()
    print(datos)


def updateFields():
    conx = sql.connect("Productos.db")
    cursor = conx.cursor()
    instruccion = f"UPDATE Producto SET Stock =1200000 WHERE name like 'calculadora'"
    cursor.execute(instruccion)
    conx.commit()
    conx.close()
  
def deleteRow():
    conx = sql.connect("Productos.db")
    cursor = conx.cursor()
    instruccion = f"DELETE FROM Producto WHERE name='"
    cursor.execute(instruccion)
    
    conx.commit()
    conx.close()

if __name__ == "__main__":
    #createBase()
    #createTable()
    #inserRow("Calculadora", 15 , 15.50)
    #inserRow("Impresora", 15 , 15.50)
    #readOrderDDed("Valor")

    Productos = [
    ("Laptop", 100, 459.99),
    ("Mause", 20, 15.99),
    ("Teclado", 5, 19.99)
]


