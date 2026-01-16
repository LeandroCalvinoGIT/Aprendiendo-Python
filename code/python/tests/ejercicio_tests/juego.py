# Clase Item: 
#   Atributos:
#       - Nombre (str)
#   Métodos:
#       - describir(): printea la clase del item
#       - usar(jugador): printea el nombre del jugador y del item 

class Item():
    def __init__(self, nombre):
        self.nombre = nombre
    
    def describir(self):
        print(f"Este item es del tipo: {self.__class__.__name__}")

    
    def usar(self, jugador):
        print(f"{jugador.nombre} está usando {self.nombre}")

# Item -> Comida: 
#   Atributos:
#       - Nombre (str)
#       - cant_cura(int)
#   Métodos:
#       - describir(): printea la clase del item
#       - usar(jugador): super y cura al jugador, elimina su herramienta y elimina a la comida del inventario

class Comida(Item):
    def __init__(self, nombre, cant_cura):
        super().__init__(nombre)
        self.cant_cura = cant_cura
    
    def usar(self, jugador):
        super().usar(jugador)
        if jugador.curar(self.cant_cura):
            jugador.herramienta = None
            jugador.eliminar_item(self)

# Item -> Herramienta: 
#   Atributos:
#       - Nombre (str)
#       - durabilidad(int)
#   Métodos:
#       - describir(): printea la clase del item
#       - usar(jugador): super y baja 1 a la durabilidad, si dur == 0 elimina herramienta e item del inventario

class Herramienta(Item):
    def __init__(self, nombre, durabilidad):
        super().__init__(nombre)
        self.durabilidad = 100
        try:
            if durabilidad <= 0:
                raise ValueError("La herramienta no tener puntos de durabilidad")
            self.durabilidad = durabilidad
        except ValueError:
            print("No se puede asignar una durabilidad menor o igual a 0, se asigna 100 por defecto")

    def usar(self, jugador):
        super().usar(jugador)
        self.durabilidad -= 1
        if self.durabilidad <= 0:
            print("No le quedan más usos a esta herramienta")
            jugador.herramienta = None
            jugador.eliminar_item(self)
            return
        print(f"La durabilidad restante de {self.nombre} es de {self.durabilidad}")

# Item -> Bloque: 
#   Atributos:
#       - Nombre (str)
#   Métodos:
#       - describir(): printea la clase del item
#       - usar(jugador): super y printea mensaje, elimina su herramienta y elimina del inventario

class Bloque(Item):
    def __init__(self, nombre):
        super().__init__(nombre)

    def usar(self, jugador):
        super().usar(jugador)
        print(f"Se coloca bloque: {self.nombre}")
        jugador.herramienta = None
        jugador.eliminar_item(self)

# JUGADOR:

# Jugador
#   Atributos:
#       - nombre (str)
#       - item_equipado (Item)
#       - vida (int)
#       - inventario(Item[]) 
#   Métodos:
#       - estado(): printea stats 
#       - 


class Jugador():
    def __init__(self, nombre, item_equipado=None, inventario=[]):
        self.nombre = nombre
        self.item_equipado = item_equipado
        self.vida = 100
        self.inventario = inventario

    def estado(self):
        print(f"-----Resumen de stats de {self.nombre}-----")
        print(f"Puntos de vida: {self.vida}")
        if self.item_equipado != None:
            print(f"Item Equipado: {self.item_equipado.nombre}")
        else:
            print("No hay ningun item equipado")
        self.__mostrar_inventario()

    
    # HERRAMIENTAS:
    def equipar_item(self, item):
        if item in self.inventario: # Chequea que el item a equipar esté en el inventario del jugador
            self.item_equipado = item
            print(f"{self.nombre} ahora tiene equipado: {item.nombre}")
        else:
            print(f"El item {item} no está en el inventario de {self.nombre}")

    def desequipar_item(self):
        self.item_equipado = None
        print(f"{self.nombre} ahora no tiene un item equipado")
        

    def usar_item_equipado(self):
        if self.item_equipado == None:
            print(f"{self.nombre} no tiene ningun item equipado")
        else: 
            self.item_equipado.usar(self)

    # INVENTARIO
    def agregar_item(self, item):
        self.inventario.append(item)
        print(f"Se agrego el item {item.nombre} al inventario de {self.nombre}")
    
    def eliminar_item(self, item):
        self.inventario.remove(item)
        print(f"Se elimino el item {item.nombre} del inventario de {self.nombre}")

    def __mostrar_inventario(self):
        if self.inventario != []:
            print(f"Inventario: ")
            for item in self.inventario:
                print(f"- {item.nombre}")
        else:
            print(f"El inventario de {self.nombre} está vacío")

    # VIDA
    def curar(self, cantidad):
        if self.vida <= 0:
            print("No se puede curar a un jugador muerto")
            return False
        elif self.vida < 100:
            if self.vida + cantidad > 100:
                print(f"{self.nombre} recupera {100 - self.vida} puntos de vida")
                self.vida = 100
            else:
                print(f"{self.nombre} recupera {cantidad} puntos de vida")
                self.vida += cantidad
            print(f"La vida de {self.nombre} es ahora {self.vida}")
            return True
        else:
            print(f"{self.nombre} ya tiene la vida al máximo! No puede comer")
            return False

    def curarse(self):
        print(f"{self.nombre} está intentando curarse")
        cantidad_cura = 0
        comidas_consumidas = []

        if self.vida == 0:
            print("No se puede curar a un jugador muerto")
            return
        
        # Recorro iterando en copia de inventario buscando comidas para curarse
        for item in list(self.inventario):
            if isinstance(item, Comida):
                # Si ya tiene la vida al máximo, no sigue consumiendo
                if self.vida >= 100:
                    print(f"{self.nombre} ya tiene la vida al máximo")
                    break
                # Equipa y usa el item comida para curarse
                self.equipar_item(item)
                self.usar_item_equipado()
                
                # Registro para prints
                comidas_consumidas.append(item.nombre)
                cantidad_cura += item.cant_cura
    
        print(f"{self.nombre} recupera un total de {cantidad_cura} puntos de vida")
        print(f"Items consumidos: {comidas_consumidas}")
    
    def recibir_danio(self, cantidad):
        if self.vida == 0:
            print(f"{self.nombre} ya está muerto, no puede seguir recibiendo daño")
        if self.vida - cantidad <= 0:
            self.vida = 0
            print(f"El jugador {self.nombre} no resiste ese ataque, y muere")
        else:
            self.vida -= cantidad
            print(f"El jugador {self.nombre} recibió {cantidad} puntos de daño, vida restante: {self.vida}")
