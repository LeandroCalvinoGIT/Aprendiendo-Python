# Aplicación de conceptos con temática Hunger games
""" class Tributo():

    #Constructor (estado inicial):
    def __init__(self, nombre, distrito):
        # Atributos:
        self.nombre = nombre
        self.distrito = distrito
        # Atributo encapsulado
        self.__isAlive = True

    def atributos(self):
        print("--------------------------------------")
        print(f"Mi nombre es ", self.nombre)
        print(f"Provengo del distrito ", self.distrito)
        if self.__isAlive:
            print("Sigo con vida")
        else:
            print("Fallecí")

    def morir(self):
        self.__isAlive = False
        print(f"{self.nombre} ha muerto")

    def matar(self, tributo):
        print(f"{self.nombre} asesino a {tributo.nombre}")
        tributo.morir()
        
        
class Vencedor(Tributo):
    def __init__(self, nombre, distrito, anioDeVictoria):
        super().__init__(nombre,distrito)
        self.anioDeVictoria = anioDeVictoria

    def puedeMentorear(self, tributo):
        if self.distrito == tributo.distrito:
            print(f"{self.nombre} puede ser mentor de {tributo.nombre}")
        else:
            print(f"{self.nombre} solo puede ser mentor de {tributo.nombre} si no hay otro vencedor del distrito {tributo.distrito} con vida")

    def atributos(self):
        super().atributos()
        print("Gane en el año: ", self.anioDeVictoria)



# Instancias una clase:

#katniss = Tributo(nombre= "Katniss Everdeen", distrito = 12)
#clove = Tributo(nombre = "Clove", distrito = 2)

peeta = Tributo("Peeta Mellark", 12)
cato = Tributo("Cato", 2)

haymitch = Vencedor("Haymitch Abernathy", 12, 50)

peeta.atributos()
cato.atributos()
haymitch.atributos()
peeta.matar(cato)

haymitch.puedeMentorear(peeta)
haymitch.puedeMentorear(cato)

print(haymitch.anioDeVictoria) """

# ==========================================================
# EJERCICIOS PYTHON - PROGRAMACIÓN ORIENTADA A OBJETOS (POO)
# TEMÁTICA: MINECRAFT
# ==========================================================


# ----------------------------------------------------------
# EJERCICIO 1 - CLASE SIMPLE
# ----------------------------------------------------------
# Crea una clase llamada Bloque
# - Debe tener un atributo llamado "tipo"
# - Al crear el bloque, se debe indicar el tipo (ej: "tierra", "piedra")
# - Crea un objeto Bloque e imprime su tipo

""" class Bloque():
    def __init__(self, tipo):
        self.tipo = tipo

tierra = Bloque("tierra")
print(tierra.tipo)"""
# ----------------------------------------------------------
# EJERCICIO 2 - MÉTODO DE INSTANCIA
# ----------------------------------------------------------
# Modifica la clase Bloque:
# - Agrega un método llamado describir
# - El método debe imprimir:
#   "Este bloque es de tipo <tipo>"
# - Llama al método desde un objeto

""" class Bloque():
    def __init__(self, tipo):
        self.tipo = tipo
    
    def describir(self):
        print(f"Este bloque es del tipo: <{self.tipo}>")

tierra = Bloque("tierra")
tierra.describir() """

# ----------------------------------------------------------
# EJERCICIO 3 - MÚLTIPLES ATRIBUTOS
# ----------------------------------------------------------
# Crea una clase llamada Herramienta
# - Atributos:
#   * nombre
#   * durabilidad
# - Método usar():
#   * Reduce la durabilidad en 1
#   * Muestra la durabilidad restante
# - Crea una herramienta y úsala varias veces

""" class Herramienta():
    def __init__(self, nombre, durabilidad):
        self.nombre = nombre
        self.durabilidad = durabilidad

    def usar(self):
        print(f"Usando {self.nombre}")
        self.durabilidad -= 1
        print(f"La durabilidad restante de {self.nombre} es de {self.durabilidad}")

pico_de_hierro = Herramienta("Pico de hierro", 750)

for n in range(1,11):
    pico_de_hierro.usar() """
# ----------------------------------------------------------
# EJERCICIO 4 - VALIDACIÓN EN EL CONSTRUCTOR
# ----------------------------------------------------------
# Modifica la clase Herramienta:
# - Si la durabilidad es menor o igual a 0:
#   * Lanza una excepción ValueError
# - Prueba crear una herramienta inválida y maneja el error

""" class Herramienta():
    def __init__(self, nombre, durabilidad):
        self.nombre = nombre
        self.durabilidad = 100
        try:
            if durabilidad <= 0:
                raise ValueError("La herramienta no tiene mas puntos de durabilidad")
            self.durabilidad = durabilidad
        except ValueError:
            print("No se puede asignar una durabilidad menor o igual a 0, se asigna 100 por defecto")

    def usar(self):
        if self.durabilidad <= 0:
            print("No le quedan más usos a esta herramienta")
        else:
            print(f"Usando {self.nombre}")
            self.durabilidad -= 1
            print(f"La durabilidad restante de {self.nombre} es de {self.durabilidad}")

pico_de_hierro = Herramienta("Pico de hierro", -45)

for n in range(1,11):
    pico_de_hierro.usar()  """

# ----------------------------------------------------------
# EJERCICIO 5 - CLASE JUGADOR
# ----------------------------------------------------------
# Crea una clase Jugador
# - Atributos:
#   * nombre
#   * vida (inicia en 100)
# - Método recibir_daño(cantidad):
#   * Resta vida
#   * La vida no puede ser menor a 0
# - Crea un jugador y aplícale daño

""" class Jugador():
    def __init__(self, nombre):
        self.nombre = nombre
        self.vida = 100

    def recibir_danio(self, cantidad):
        if self.vida - cantidad < 0:
            self.vida = 0
            print(f"El jugador {self.nombre} no resiste ese ataque, y muere")
        else:
            self.vida -= cantidad
            print(f"El jugador {self.nombre} recibió {cantidad} puntos de daño, vida restante: {self.vida}")

steve = Jugador("Steve")
steve.recibir_danio(50)
steve.recibir_danio(60) """
# ----------------------------------------------------------
# EJERCICIO 6 - RELACIÓN ENTRE OBJETOS
# ----------------------------------------------------------
# Modifica Jugador:
# - Agrega un atributo "herramienta" (puede ser None)
# - Agrega un método equipar(herramienta)
# - Agrega un método usar_herramienta()
#   * Usa la herramienta si existe
#   * Si no hay herramienta, muestra un mensaje

""" class Jugador():
    def __init__(self, nombre, herramienta):
        self.nombre = nombre
        self.herramienta = herramienta
        self.vida = 100
    
    def equipar_item(self, herramienta):
        self.herramienta = herramienta
        print(f"{self.nombre} ahora tiene equipado: {herramienta}")

    def usar_item_equipado(self):
        if self.herramienta == None:
            print(f"{self.nombre} no tiene ninguna herramienta equipada")
        else:
            print(f"{self.nombre} usa {self.herramienta}")
            self.herramienta.usar()

    def recibir_danio(self, cantidad):
        if self.vida - cantidad < 0:
            self.vida = 0
            print(f"El jugador {self.nombre} no resiste ese ataque, y muere")
        else:
            self.vida -= cantidad
            print(f"El jugador {self.nombre} recibió {cantidad} puntos de daño, vida restante: {self.vida}")

steve = Jugador("Steve", None)

steve.usar_item_equipado()

steve.equipar_item(pico_de_hierro)

steve.usar_item_equipado() """

# ----------------------------------------------------------
# EJERCICIO 7 - INVENTARIO (LISTAS + POO)
# ----------------------------------------------------------
# Modifica Jugador:
# - Agrega un atributo inventario (lista)
# - Métodos:
#   * agregar_item(item)
#   * mostrar_inventario()
# - Guarda bloques y herramientas en el inventario
""" 
class Jugador():
    def __init__(self, nombre, herramienta, inventario):
        self.nombre = nombre
        self.herramienta = herramienta
        self.vida = 100
        self.inventario = inventario
    
    # HERRAMIENTAS:
    def equipar_item(self, herramienta):
        self.herramienta = herramienta
        print(f"{self.nombre} ahora tiene equipado: {herramienta}")

    def usar_item_equipado(self):
        if self.herramienta == None:
            print(f"{self.nombre} no tiene ninguna herramienta equipada")
        else:
            print(f"{self.nombre} usa {self.herramienta}")
            self.herramienta.usar()

    # INVENTARIO
    def agregar_item(self, item):
        self.inventario.append(item)
        print(f"Se agrego el item {item} al inventario de {self.nombre}")

    def mostrar_inventario(self):
        if self.inventario != []:
            print(f"Inventario de {self.nombre}")
            print(self.inventario)
        else:
            print(f"El inventario de {self.nombre} está vacío")

    # VIDA
    def recibir_danio(self, cantidad):
        if self.vida - cantidad < 0:
            self.vida = 0
            print(f"El jugador {self.nombre} no resiste ese ataque, y muere")
        else:
            self.vida -= cantidad
            print(f"El jugador {self.nombre} recibió {cantidad} puntos de daño, vida restante: {self.vida}")

steve = Jugador("Steve", None, [])

steve.mostrar_inventario()
steve.agregar_item(pico_de_hierro)
steve.agregar_item(tierra)
steve.mostrar_inventario() """
# ----------------------------------------------------------
# EJERCICIO 8 - HERENCIA
# ----------------------------------------------------------
# Crea una clase Enemigo
# - Atributos:
#   * nombre
#   * daño
# - Método atacar(jugador)
#
# Crea una subclase Zombie que:
# - Tenga más daño que un enemigo normal
# - Sobrescriba el método atacar con un mensaje especial

""" class Enemigo():
    def __init__(self, nombre, danio):
        self.nombre = nombre
        self.danio = danio
    
    def atacar(self, jugador):
        print(f"{self.nombre} ataca a {jugador.nombre}")
        jugador.recibir_danio(self.danio)

class Zombie(Enemigo):
    def __init__(self, nombre, danio, edad):
        self.edad = edad
        super().__init__(nombre, danio)
        if edad == "bebe":
            self.danio *= 2
        elif edad == "adulto":
            self.danio *= 1.5
        

    def atacar(self, jugador):
        print(f"{self.nombre} muerde el cerebro de {jugador.nombre}")
        jugador.recibir_danio(self.danio) """


# ----------------------------------------------------------
# EJERCICIO 9 - POLIMORFISMO
# ----------------------------------------------------------
# Crea otra subclase de Enemigo llamada Esqueleto
# - Tiene su propio daño
# - Ataca de forma distinta
#
# Crea una lista de enemigos (Zombie y Esqueleto)
# - Recorre la lista
# - Todos deben atacar al jugador
# - Sin preguntar el tipo de enemigo (polimorfismo)

""" class Esqueleto(Enemigo):
    def __init__(self, nombre, cantidad_flechas):
        self.cantidad_flechas = cantidad_flechas
        if cantidad_flechas > 30:
            danio = 2
        else:
            danio = 1
        super().__init__(nombre, danio)

    def atacar(self, jugador):
        print(f"{self.nombre} dispara a {jugador.nombre}")
        for flecha in range(1,self.cantidad_flechas+1):
            jugador.recibir_danio(self.danio)

zombie1 = Zombie("Frankie", 20, "adulto")
esqueleto1 = Esqueleto("Larry", 40)
enemigos = [zombie1, esqueleto1]

for enemigo in enemigos:
    enemigo.atacar(steve) """
# ----------------------------------------------------------
# EJERCICIO 10 - MINI PROYECTO INTEGRADOR
# ----------------------------------------------------------
# Sistema básico de supervivencia en Minecraft
#
# Requisitos:
#
# - Clase Jugador:
#   * nombre, vida, inventario
#   * métodos para:
#     - recibir daño
#     - curarse
#     - mostrar estado
#
# - Clase Enemigo (y al menos 2 subclases)
#   * atacan al jugador
#
# - Clase Item:
#   * nombre, tipo (bloque / comida / herramienta)
#
# - Clase Comida (hereda de Item):
#   * tiene valor de curación
#
# Flujo del programa:
# - Crear jugador
# - Crear enemigos
# - Simular ataques
# - Agregar comida al inventario
# - Curar al jugador usando objetos
#
# Objetivo:
# - Integrar:
#   * clases
#   * herencia
#   * listas
#   * métodos
#   * control de estado
#
# No importa que sea simple, importa que funcione.

# ITEM
class Item():
    def __init__(self, nombre):
        self.nombre = nombre
    
    def describir(self):
        print(f"Este item es del tipo: {self.__class__.__name__}")

    
    def usar(self, jugador):
        print(f"{jugador.nombre} está usando {self.nombre}")

class Comida(Item):
    def __init__(self, nombre, cant_cura):
        super().__init__(nombre)
        self.cant_cura = cant_cura
    
    def usar(self, jugador):
        super().usar(jugador)
        if jugador.curar(self.cant_cura):
            jugador.herramienta = None
            jugador.eliminar_item(self)

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

class Bloque(Item):
    def __init__(self, nombre):
        super().__init__(nombre)

    def usar(self, jugador):
        super().usar(jugador)
        print(f"Se coloca bloque: {self.nombre}")
        jugador.herramienta = None
        jugador.eliminar_item(self)

# JUGADOR:
class Jugador():
    def __init__(self, nombre, item_equipado, inventario):
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
        if item in self.inventario:
            self.item_equipado = item
            print(f"{self.nombre} ahora tiene equipado: {item.nombre}")

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
        if self.vida == 0:
            print("No se puede curar a un jugador muerto")
            return False
        elif self.vida < 100:
            self.vida += cantidad
            if self.vida > 100:
                self.vida = 100
            print(f"{self.nombre} recupera {cantidad} puntos de vida")
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

# ENEMIGOS
class Enemigo():
    def __init__(self, nombre, danio):
        self.nombre = nombre
        self.danio = danio
    
    def atacar(self, jugador):
        print(f"{self.nombre} ataca a {jugador.nombre}")
        jugador.recibir_danio(self.danio)

class Zombie(Enemigo):
    def __init__(self, nombre, danio, edad):
        self.edad = edad
        super().__init__(nombre, danio)
        if edad == "bebe":
            self.danio *= 2
        elif edad == "adulto":
            self.danio *= 1.5
        

    def atacar(self, jugador):
        print(f"{self.nombre} muerde el cerebro de {jugador.nombre}")
        jugador.recibir_danio(self.danio)

class Esqueleto(Enemigo):
    def __init__(self, nombre, cantidad_flechas):
        self.cantidad_flechas = cantidad_flechas
        if cantidad_flechas > 30:
            danio = 2
        else:
            danio = 1
        super().__init__(nombre, danio)

    def atacar(self, jugador):
        print(f"{self.nombre} dispara a {jugador.nombre}")
        for flecha in range(1,self.cantidad_flechas+1):
            jugador.recibir_danio(self.danio)


# INSTANCACIÓN

# JUGADORES
steve = Jugador("Steve", None, [])

# ENEMIGOS
zombie1 = Zombie("Frankie", 20, "adulto")
esqueleto1 = Esqueleto("Larry", 40)
enemigos = [zombie1, esqueleto1]

# ITEMS
    # COMIDAS
pan = Comida("Pan", 20)
papa = Comida("Papa", 15)
manzana_dorada = Comida("Manzana Dorada", 100)

    # HERRAMIENTAS
espada_de_piedra = Herramienta("Espada de Piedra", 150)

    # BLOQUES
obsidiana = Bloque("Obsidiana")

items = [pan, espada_de_piedra, papa, obsidiana, manzana_dorada]

# INICIO DE SIMULACIÓN

steve.agregar_item(espada_de_piedra)
steve.agregar_item(obsidiana)
steve.agregar_item(pan)
steve.agregar_item(papa)
steve.agregar_item(manzana_dorada)
steve.estado()

esqueleto1.atacar(steve)
steve.estado()

steve.usar_item_equipado()
steve.equipar_item(manzana_dorada)
steve.usar_item_equipado()
steve.estado()

zombie1.atacar(steve)
steve.estado()

steve.curarse()
steve.estado()

steve.equipar_item(obsidiana)
steve.usar_item_equipado()

steve.equipar_item(manzana_dorada)

steve.equipar_item(espada_de_piedra)
steve.usar_item_equipado()

steve.estado()
# ==========================================================
# FIN DE LOS EJERCICIOS
# ==========================================================

