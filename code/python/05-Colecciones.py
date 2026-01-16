# ==========================================================
# EJERCICIOS PYTHON - COLECCIONES
# CONTEXTO: LOS JUEGOS DEL HAMBRE
# LISTAS, TUPLAS, SETS, DICCIONARIOS
# ==========================================================


# -------------------------------
# NIVEL 1 - LISTAS
# -------------------------------

# 1) Tributos del Distrito 12
# Tenes la siguiente lista:
tributos = ["Katniss", "Peeta"]

# a) Mostra el primer tributo

print(tributos[0])
# b) Mostra el ultimo tributo
print(tributos[-1])
# c) Agrega "Gale" a la lista
tributos.append("Gale")
print(tributos)
# d) Elimina "Gale"
tributos.remove("Gale")
# e) Mostra cuantos tributos hay
print(len(tributos))


# 2) Orden de entrenamiento
# Tenes la siguiente lista:
entrenamiento = ["correr", "lanzar flechas", "escalar"]

# a) Mostra solo las dos primeras actividades
print(entrenamiento[:2])
# b) Reemplaza "escalar" por "camuflaje"
entrenamiento[2] = "camuflaje"
# c) Mostra la lista final
print(entrenamiento)

# -------------------------------
# NIVEL 2 - TUPLAS
# -------------------------------

# 3) Arena de los juegos
# La arena tiene coordenadas fijas:
arena = (45, 78)

# a) Mostra la coordenada X
print(arena[0])
# b) Mostra la coordenada Y
print(arena[1])
# c) Explica en un comentario por que conviene usar una tupla
""" Conviene utilizar una tupla ya que al ser coordenadas FIJAS (que no cambian), no es necesario que 
se utilice una estructura donde se puedan modificar los datos (como una lista), y la tupla tiene la ventaja
de ser mas optimizada que otras estructuras."""

# -------------------------------
# NIVEL 2 - SETS
# -------------------------------

# 4) Habilidades de Katniss
# Katniss aprende habilidades durante el entrenamiento:
habilidades = {"arco", "caza", "supervivencia"}

# a) Agrega "arco" nuevamente
habilidades.add("arco")
# b) Agrega "camuflaje"
habilidades.add("camuflaje")
# c) Mostra el set final
print(habilidades)
# d) Explica en un comentario por que "arco" no se duplica
""" "arco" no se duplica ya que los sets son colecciones sin repetidos. """

# 5) Tributos vivos
vivos = {"Katniss", "Peeta", "Cato", "Foxface"}
eliminados = {"Cato", "Foxface"}

# a) Mostra que tributos siguen vivos
# b) Guarda el resultado en una nueva variable

siguenVivos = vivos - eliminados
print(siguenVivos)

# -------------------------------
# NIVEL 3 - DICCIONARIOS
# -------------------------------

# 6) Perfil de tributo
katniss = {
    "nombre": "Katniss Everdeen",
    "distrito": 12,
    "arma": "arco",
    "viva": True
}

# a) Mostra el nombre
print(katniss.get("nombre"))
# b) Cambia el arma a "trampa"
katniss["arma"]= "trampa"
# c) Agrega la clave "puntuacion" con valor 11
katniss.update({"puntuacion":11})
# d) Mostra el diccionario completo
print(katniss)


# -------------------------------
# NIVEL 4 - VARIOS TRIBUTOS
# -------------------------------

# Ahora trabajamos con varios tributos
tributos = [
    {
        "nombre": "Katniss",
        "distrito": 12,
        "arma": "trampa",
        "vive": True
    },
    {
        "nombre": "Peeta",
        "distrito": 12,
        "arma": "fuerza",
        "vive": True
    },
    {
        "nombre": "Cato",
        "distrito": 2,
        "arma": "espada",
        "vive": False
    }
]

# a) Mostra el nombre del segundo tributo
print(tributos[1].get("nombre"))
# b) Mostra el distrito del tributo llamado "Cato"
print(tributos[-1].get("distrito"))
# c) Cambia el estado de "Peeta" a no vivo
tributos[1]["vive"]= False
# d) Agrega un nuevo tributo con los datos que quieras
tributos.append(
        {
        "nombre": "Clove",
        "distrito": 2,
        "arma": "cuchillos",
        "vive": False
        }
)

print(tributos)

# -------------------------------
# EJERCICIO 5 - CONSULTAS BASICAS
# -------------------------------

# Usando la lista de tributos:
# PISTA: vas a necesitar recorrer la lista con un bucle

# a) Mostra SOLO los tributos que esten vivos
for tributo in tributos:
    if tributo.get("vive"):
        print(tributo.get("nombre")+ " sigue con vida")
# b) Mostra SOLO los nombres de los tributos del distrito 12
for tributo in tributos:
    if tributo.get("distrito") == 12:
        print(tributo.get("nombre"))
# c) Mostra cuántos tributos hay en total
print(len(tributos))


# ==========================================================
# FIN DEL MINI PROYECTO
# ==========================================================