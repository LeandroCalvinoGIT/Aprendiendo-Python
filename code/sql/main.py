import sqlite3

conexion = sqlite3.connect("base_de_datos.db")

cursor = conexion.cursor()

# Solo se ejecuta una vez o da error
#cursor.execute("""CREATE TABLE estudiantes(
#                                Nombre TEXT,
#                                Apellido TEXT,
#                                Edad INT,
#                                Email TEXT,
#                                Id VARCHAR(20))
#                                                """)
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY,
    nombre TEXT,
    edad INTEGER,
    ciudad TEXT
)
""")

#cursor.execute("""
"""INSERT INTO usuarios (nombre, edad, ciudad)
VALUES 
    ('Ana', 30, 'Córdoba'),
    ('Juan', 25, 'Buenos Aires'),
    ('Lucía', 35, 'Rosario'),
    ('Pedro', 28, 'Córdoba')
"""
cursor.execute("""
CREATE TABLE IF NOT EXISTS animales(
        id )
               
               """)

conexion.commit()

# cursor.execute("INSERT INTO estudiantes()")

print("Se ha creado la tabla")

conexion.close()