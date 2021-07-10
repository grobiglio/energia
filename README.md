# energia
 Código para seguimiento de energía disponible en Cashpower.

Este programa inicia con un menú de bienvenida que ofrece las siguientes opciones:
1. Reporte de estado
2. Lectura de energía
3. Carga de energía
4. Salir
En caso de que se seleccionen las opciones 1, 2 o 3 se vuelve al menú principal después de ejecutar la operación seleccionada.

**Opción 1:** Informa:
* Próxima fecha de cobro
* El consumo (en KWh) promedio de energía por hora y por día durante el corriente mes
* El gasto (en pesos) promedio por hora y por día durante el corriente mes
* Si sobra o falta energía para llegar a la fecha de cobro. En caso de que falte energía, informa cuanto falta, en KWh y en pesos.

**Opción 2:** Requiere el ingreso de la cantidad de energía remanente que figura en la pantalla del Cashpower.
![Pantalla de Cashpower](/imagenes/cashpower.jpg)
Tras el ingreso del valor se da el reporte de estado. Cuando se ingrese la lectura el sistema automáticamente gardará la fecha y la hora, asimismo, guardará una carga de 0 Kwh.

**Opción 3:** Requiere ingreso de carga de energía, luego requiere ingreso de energía remanente. Tras ambos ingresos se da el reporte de estado. En este caso el sistema guardará la carga, lectura y fecha y hora.

**Opción 4:** Sale del sistema.

*NOTA 1:* En caso de que tenga lugar la primera lectura de energía del mes, el programa, automáticamente cargará una lectura a las 0:00 hs de primer día del corriente mes con un valor interpolado en forma lineal entre la carga actual y la última del mes pasado.

*NOTA 2:* Como los cálculos se basan en el promedio de consumo del mes en curso, mientras más lecturas se hagan, más precisas serán las predicciones.

*NOTA 3:* La información histórica de lecturas y cargas se almacenan en un archivo de texto según la siguiente tabla:

|Fecha|Lectura|Carga|Consumo|
|-----|-------|-----|-------|
|Fecha y hora de lectura|Valor de lectura (en Kwh)|Valor de carga (en Kwh)|Consumo calculado entre la lectura anterior y la actual|