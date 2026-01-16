# ==================================================
# EJERCICIO DE TESTING - SISTEMA DE ITEMS Y JUGADOR
# ==================================================
#
# OBJETIVO:
# Practicar testing en Python aplicando:
# - assert
# - unittest
# - setUp
# - distintos métodos assert
#
# El código a testear se encuentra en:
# - juego.py
#
# Crear este archivo:
# - test_juego.py
#
# ==================================================
# ORGANIZACIÓN
# ==================================================
#
# - Importar las clases desde juego.py
# - Usar unittest.TestCase
# - Ejecutar los tests con:
#   if __name__ == "__main__":
#       unittest.main()
#
# ==================================================
# PARTE 1 - TESTS BÁSICOS CON assert
# ==================================================
#
# 1) TEST CREACIÓN DE ITEM
# - Crear un Item con nombre "Piedra"
# - Verificar con assert que:
#   * El atributo nombre existe
#   * El nombre sea "Piedra"
#
# --------------------------------------------------
#
# 2) TEST CREACIÓN DE COMIDA
# - Crear una Comida("Manzana", 20)
# - Verificar que:
#   * Es instancia de Item
#   * Tiene atributo cant_cura
#   * cant_cura == 20
#
# --------------------------------------------------
#
# 3) TEST HERRAMIENTA CON DURABILIDAD INVÁLIDA
# - Crear una Herramienta("Pico", 0)
# - Verificar que:
#   * La durabilidad final sea 100
#
# ==================================================
# PARTE 2 - UNIT TESTING CON unittest
# ==================================================
#
# Crear una clase que herede de unittest.TestCase
#
# ==================================================
# PARTE 3 - setUp
# ==================================================
#
# 4) CONFIGURACIÓN COMÚN (setUp)
# - Crear en setUp:
#   * Un jugador llamado "Alex"
#   * Vida inicial 100
#   * Inventario vacío
#   * Sin item equipado
#
# - Todos los tests deben usar este jugador base
#
# ==================================================
# PARTE 4 - TESTS DE VIDA Y CURACIÓN
# ==================================================
#
# 5) TEST CURACIÓN BÁSICA
# - Reducir la vida del jugador a 50
# - Llamar a curar(30)
# - Verificar que:
#   * El método devuelve True
#   * La vida final sea 80
#
# --------------------------------------------------
#
# 6) TEST CURACIÓN CON VIDA COMPLETA
# - Asegurar que la vida sea 100
# - Llamar a curar(20)
# - Verificar que:
#   * El método devuelve False
#   * La vida siga siendo 100
#
# ==================================================
# PARTE 5 - TESTS DE INVENTARIO
# ==================================================
#
# 7) TEST AGREGAR Y ELIMINAR ITEMS
# - Crear un Bloque("Tierra")
# - Agregarlo al inventario
# - Verificar que esté en el inventario
# - Eliminarlo
# - Verificar que el inventario quede vacío
#
# --------------------------------------------------
#
# 8) TEST EQUIPAR ITEM
# - Agregar una Herramienta al inventario
# - Equiparla
# - Verificar que item_equipado sea ese item
#
# ==================================================
# PARTE 6 - TESTS DE USO DE ITEMS
# ==================================================
#
# 9) TEST USO DE HERRAMIENTA
# - Crear una Herramienta con durabilidad 2
# - Equiparla
# - Usarla una vez
# - Verificar que la durabilidad sea 1
# - Usarla nuevamente
# - Verificar que:
#   * El item se elimine del inventario
#   * El jugador quede sin item equipado
#
# --------------------------------------------------
#
# 10) TEST USO DE COMIDA
# - Reducir la vida del jugador
# - Agregar una Comida al inventario
# - Equiparla y usarla
# - Verificar que:
#   * La vida aumente
#   * La comida se elimine del inventario
#
# ==================================================
# PARTE 7 - TESTS DE TIPO Y COMPORTAMIENTO
# ==================================================
#
# 11) TEST DE TIPO DE ITEMS
# - Verificar con assertIsInstance que:
#   * Comida es instancia de Item
#   * Bloque es instancia de Item
#
# --------------------------------------------------
#
# 12) TEST RECIBIR DAÑO MORTAL
# - Aplicar daño mayor a la vida
# - Verificar que:
#   * La vida quede en 0
#
# ==================================================
# PARTE 8 - TEST DE FLUJO COMPLETO
# ==================================================
#
# 13) TEST MÉTODO curarse()
# - Agregar varias comidas al inventario
# - Reducir la vida del jugador
# - Llamar a curarse()
# - Verificar que:
#   * La vida final no supere 100
#   * Las comidas se eliminen del inventario
#
# ==================================================
# BONUS (OPCIONAL)
# ==================================================
#
# - Testear que un jugador muerto no pueda curarse
# - Identificar métodos difíciles de testear
#   (prints, efectos colaterales, estados mutables)
#
# ==================================================
# FIN DEL EJERCICIO
# ==================================================

# IMPORTS
import unittest
from juego import *

# 1)
piedra = Item("Piedra")
assert piedra.nombre == "Piedra"

#2)
manzana = Comida("Manzana", 20)
assert isinstance(manzana, Item) is True
try:
    assert manzana.cant_cura == 20
except AttributeError:
    print("El objeto no cuenta con el atributo")

#3)
pico = Herramienta("Pico", 0)
assert pico.durabilidad == 100

# PARTE 2
class testear_juego(unittest.TestCase):

    #4)
    def setUp(self):
        print("Reiniciando jugador de testeo.")
        self.jugador = Jugador("Alex")
        self.jugador.estado()

    def tearDown(self):
        pass
    
    #5)
    def test_curacion_basica(self):
        print("\n############################ Test Curacion Valida ################################\n")
        self.jugador.recibir_danio(50)
        self.assertTrue(self.jugador.curar(30))
        self.assertEqual(self.jugador.vida, 80)

    #6)
    def test_curacion_con_vida_completa(self):
        print("\n############################ Test Curacion Invalida ################################\n")
        self.assertFalse(self.jugador.curar(20))
        self.assertEqual(self.jugador.vida, 100)

# PARTE 3:
    #7)
    def test_modificar_inventario(self):
        print("\n############################ Test Modificar Inventario ################################\n")
        #crear item
        tierra = Bloque("Tierra")
        #verificar que se agrega correctamente al inventario
        self.jugador.agregar_item(tierra)
        self.assertIn(tierra, self.jugador.inventario)
        #verificar que se elimina correctamente del inventario
        self.jugador.eliminar_item(tierra)
        self.assertNotIn(tierra, self.jugador.inventario)
        self.assertEqual(len(self.jugador.inventario), 0)
    
    #8)
    def test_equipar_item_valido(self):
        print("\n############################ Test Equipar Item Valido ################################\n")
        #agregar herramienta
        pala = Herramienta("Pala", 100)
        self.jugador.agregar_item(pala)
        self.jugador.equipar_item(pala)
        self.assertEqual(self.jugador.item_equipado, pala)
        self.jugador.desequipar_item()
        self.jugador.eliminar_item(pala)

    #9)
    def test_usar_herramienta(self):
        print("\n############################ Test Usar Herramienta ################################\n")
        #crear herramienta
        fosforo = Herramienta("Fósforo", 2)
        #equiparla
        self.jugador.agregar_item(fosforo)
        self.jugador.equipar_item(fosforo)
        #usarla 1 vez y verificar
        self.jugador.usar_item_equipado()
        self.assertEqual(self.jugador.item_equipado.durabilidad, 1)
        #usarla otra vez y verificar
        self.jugador.usar_item_equipado()
        self.assertEqual(len(self.jugador.inventario), 0)

    #10)
    def test_usar_comida(self):
        print("\n############################ Test Usar Comida ################################\n")
        #bajar vida
        self.jugador.recibir_danio(50)
        #crear y equipar comida
        papa = Comida("Papa", 20)
        self.jugador.agregar_item(papa)
        #equipar y usar
        self.jugador.equipar_item(papa)
        self.jugador.usar_item_equipado()
        #verificar
        self.assertEqual(self.jugador.vida, 70)
        self.assertEqual(len(self.jugador.inventario), 0)

# PARTE 5
    #11)
    def test_tipos_de_items(self):
        print("\n############################ Test Tipos de Items ################################\n")
        comida = Comida("a",1)
        bloque = Bloque("a")
        self.assertIsInstance(comida,Item)
        self.assertIsInstance(bloque,Item)

    #12)
    def test_danio_mortal(self):
        print("\n############################ Test Daño Mortal ################################\n")
        self.jugador.recibir_danio(150)
        self.assertEqual(self.jugador.vida, 0)

# PARTE 6 
    #13)
    def test_curarse(self):
        print("\n############################ Test Curarse ################################\n")
        #crear y agregar comidas
        comida1 = Comida("Manzana", 10)
        comida2 = Comida("Pera", 30)
        comida3 = Comida("Banana", 69)
        self.jugador.agregar_item(comida1)
        self.jugador.agregar_item(comida2)
        self.jugador.agregar_item(comida3)
        #reducir vida
        self.jugador.recibir_danio(99)
        #curarse
        self.jugador.curarse()
        #verificar
        self.assertFalse(self.jugador.vida > 100)
        self.assertEqual(len(self.jugador.inventario), 0)

    # BONUS
    def test_no_revivir(self):
        print("\n############################ Test No Revivir ################################\n")
        self.jugador.recibir_danio(100)
        self.assertFalse(self.jugador.curar(10))
        self.assertEqual(self.jugador.vida, 0)


""" 
Son dificiles de testear los métodos mostrar inventario o estado, ya que no se puede comprobar que se imprima
correctamente el mensaje, solo que los valores coincidan con los asignados.
"""

if __name__ == '__main__':
    unittest.main()