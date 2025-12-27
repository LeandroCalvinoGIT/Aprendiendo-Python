# ==================================================
# PARTE 1 - CLASE JUGADOR (POO)
# ==================================================
#
# Crear una clase llamada Jugador
#
# La clase debe tener:
# - Atributos:
#   * nombre (str)
#   * nivel (int)
#   * vida (int)
#   * inventario (lista de strings)
#
# - Métodos:
#   * __init__
#   * mostrar_info() -> imprime todos los datos del jugador
#   * subir_nivel() -> aumenta el nivel en 1
#   * recibir_daño(cantidad) -> reduce la vida sin que baje de 0
#
# Validaciones:
# - nombre no puede estar vacío
# - nivel y vida deben ser enteros positivos
#
# Manejar errores con excepciones donde corresponda
#
# ==================================================
# PARTE 2 - FUNCIONES DE UTILIDAD (FUNCIONES + STRINGS)
# ==================================================
#
# Crear funciones que:
#
# 1) Soliciten datos al usuario:
#    - Nombre del jugador
#    - Nivel
#    - Vida
#    - Inventario separado por comas
#
# 2) Limpien los datos ingresados:
#    - strip()
#    - lower() o capitalize() para nombres
#    - split(",") para inventario
#
# 3) Validen:
#    - Que nivel y vida sean numéricos
#    - Que el inventario tenga al menos un item
#
# Si hay errores:
# - Mostrar mensajes claros
# - Evitar que el programa se rompa


nombres_por_defecto = ["Steve", "Juan", "Mary", "Alex"]

class Jugador():
    def __init__(self, nombre= nombres_por_defecto.choice(), nivel=0, vida=100, inventario=[]):
        # nombre no puede estar vacío
        if nombre != "":
            self.nombre = nombre
        else:
            print("El nombre del jugador no puede estar vacío, asignando nombre por defecto")
        # nivel y vida deben ser enteros positivos
        if nivel >= 0:
            self.nivel= nivel
        else:
            print("El nivel del jugador no puede ser negativo, asignando nivel por defecto (0)")
        if vida >= 0:
            self.vida = vida
        else:
            print("La vida del jugador no puede ser negativa, asignando nivel por defecto (100)")
        self.inventario = inventario
    
    # Imprime todos los datos del jugador
    def mostrar_info(self):
        print("-----Resumen de Jugador-----")
        print(f"Nombre: {self.nombre}")
        print(f"Nivel: {self.nivel}")
        print(f"Puntos de vida: {self.vida}")
        print(f"Inventario: {self.inventario}")
    
    # Aumenta el nivel en 1
    def subir_nivel(self):
        self.nivel+=1
        print(f"El nivel ah aumentado! Nivel actual: {self.nivel}")

    # Reduce la vida sin que baje de 0
    def recibir_danio(self,cantidad):
        if self.vida == 0:
            print(f"El jugador {self.nombre} ya está muerto, no puede seguir recibiendo daño")
        if self.vida - cantidad <= 0:
            self.vida = 0
            print(f"El jugador {self.nombre} no resiste ese ataque, y muere")
        else:
            self.vida -= cantidad
            print(f"El jugador {self.nombre} recibió {cantidad} puntos de daño, vida restante: {self.vida}")
