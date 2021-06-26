# energia
 Código para seguimiento de energía disponible en Cashpower.

Este programa inicia con un menú de bienvenida que ofrece las siguientes opciones:
1. Reporte de estado
2. Ingresar lectura de energía
3. Ingresar carga de energía
4. Salir

**Opción 1:** Informa:
* Próxima fecha de cobro
* El consumo promedio de energía por hora y por día durante el corriente mes
* El gasto promedio por hora y por día durante el corriente mes
* Si sobra o falta energía para llegar a la fecha de cobro. En caso de que falte energía, informa cuanto falta, en KWh y en pesos.

**Opción 2:** Permite el ingreso de la lectura de energía y después da el reporte de estado. Cuando se ingrese la lectura el sistema automáticamente gardará la fecha y la hora, asimismo, guardará una carga de 0 Kwh.

**Opción 3:** Permite ingreso de carga de energía, luego solicita lectura, tras ello da el reporte de estado. En este caso el sistema guardará la carga, lectura y fecha y hora.

*NOTA 1:* En caso de que tenga lugar la primera lectura de energía del mes, el programa, automáticamente cargará una lectura a las 0:00 hs de primer día del corriente mes con un valor interpolado en forma lineal entre la carga actual y la última del mes pasado.

*NOTA 2:* Como los cálculos se basan en el promedio de consumo del mes en curso, mientras más lecturas se hagan, más precisas serán las predicciones.

*NOTA 3:* La información histórica de lecturas y cargas se almacenan en un archivo de texto según la siguiente tabla:

|Fecha                  |Lectura                  |Carga                  |Consumo                        |
|-----------------------|-------------------------|-----------------------|-------------------------------|
|Fecha y hora de lectura|Valor de lectura (en Kwh)|Valor de carga (en Kwh)|Consumo calculado entre        |
|                       |                         |                       |la lectura anterior y la actual|