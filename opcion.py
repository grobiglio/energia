"""Administra las opciones de menú requeridas al usuario e ingresadas
por el usuario.
"""

class Opcion:
    def __init__(self) -> None:
        self.opciones_validas = ""
        self.opcion_escogida = ""

    def set_opciones_validas(self, opciones_validas: list):
        """Configura las opciones válidas que puede ingresar el usuario.

        Parámetros:
        -----------
        opciones_validas: list
            Lista de strings con las opciones válidas
        """
        self.opciones_validas = opciones_validas

    def solicitar_opcion(self):
        """Solicita al usuario el ingreso de una opción de menú.
        Después de ingresada verifica si existe correspondencia con
        alguna de las opciones válidas.
        
        Salida:
        -------
        opcion_escogida: int
            Entero que corresponde a la opcion escogida
        """
        self.opcion_escogida = int(input("Ingresar la opción de menú deseada: "))
        opcion_valida = self.opcion_escogida in self.opciones_validas
        if not(opcion_valida):
            print("Por favor, ingrese una de las opciones disponibles.")
            return
        return opcion_valida
