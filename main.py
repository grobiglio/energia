from opcion import Opcion

opcion = Opcion()
opciones_validas = [1, 2, 3, 4, 5]
opcion.set_opciones_validas(opciones_validas)
opcion.solicitar_opcion()

print("""
############# MENU #############
--------------------------------
1. Reporte de estado
2. Lectura de energía
3. Carga de energía
4. Salir
5. Cargar próxima fecha de cobro
""")

# TODO 1. Crear una clase Opcion con los siguientes atributos y métdodos:
# ATRIBUTO: opcion: valores 1 a 5
# METODO: solicitar_opcion: solicita al usuario que igrese una opción
# METODO: verificar_opcion: verifica si es una opción válida. Si es una opción válida devuelve
# el entero correspondiente, si la opción no es válida da un mensaje de error y devuelve el
# valor None.

# La carga de la próxima fecha de cobro es temporal, cuando se pueda definir
# automáticamente se eliminará esta opción.

# El codigo que se muestra abajo queda obsoleto y guardado en el commit del 9/7/2021
"""
import energia
import fechas

def mostrar_menu():
    print ("""
"""
    Programa para monitoreo de consumo de energía
    ---------------------------------------------
    \t1. Mostrar reporte de estado
    \t2. Ingresar lectura de energía
    \t3. Ingresar carga de energía
    \t4. Salir
    ---------------------------------------------
"""
"""
)
    return input('Ingresar acción deseada (1 a 4): ')

opcion_incorrecta = True
while opcion_incorrecta:
    seleccion = mostrar_menu()
    opcion_incorrecta = seleccion!='1' and seleccion!='2' and seleccion!='3' and seleccion!='4'
    print ("\nLa opción ingresada no es válida, vuelva a intentarlo." if opcion_incorrecta else "")

if seleccion=='1':
    corr_mes_y_anio = fechas.obtener_corriente_mes()
    prox_mes_y_anio = fechas.averiguar_proximo_mes(corr_mes_y_anio[0])
    fecha_de_cobro = fechas.averiguar_fecha_de_cobro(prox_mes_y_anio)
    energia.presentar_reporte(corr_mes_y_anio[0], fecha_de_cobro)
elif seleccion=='2':
    lectura = energia.ingresar_lectura()
    print (f'\nLa lectura es de {lectura} Kwh.')
elif seleccion=='3':
    carga = energia.ingresar_carga()
    lectura = energia.ingresar_lectura()
    print (f'\nLa carga es de {carga} Kwh.')
    print (f'\nLa lectura es de {lectura} Kwh.')
else:
    print ('Salir.')

input ('\nPresionar ENTER para salir.')
"""