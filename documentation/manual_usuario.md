# Manual de Usuario

## 1. Introducción

Bienvenido al sistema de monitoreo de calidad del aire. Este manual le ayudará a utilizar la aplicación para consultar y analizar los niveles de calidad del aire en tiempo real.

## 2. Iniciar la Aplicación

Para comenzar a utilizar la aplicación, primero debe acceder a la interfaz web. Abra un navegador y diríjase a la siguiente URL: `http://127.0.0.1:5001`.

## 3. Consultar los Datos de un Sensor

### 3.1 Ingresar Datos
- **ID del Sensor**: Ingrese el identificador del sensor, por ejemplo, `SOG0181`.
- **Fecha**: Seleccione una fecha específica usando el selector de fechas.

### 3.2 Visualizar Resultados
- Presione el botón **Consultar** para ver los resultados.
- Los datos aparecerán en una **tabla**, mostrando los valores para PM2.5, PM10, CO2, CO y VOC.
- Los resultados también se mostrarán en **gráficos interactivos** para facilitar la interpretación.

## 4. Interpretación de los Datos

### Parámetros Monitoreados:
- **PM2.5 y PM10**: Partículas finas que pueden ser perjudiciales para la salud. Se miden en µg/m³.
- **CO2**: Nivel de dióxido de carbono. Altos niveles indican poca ventilación.
- **CO**: Monóxido de carbono, tóxico en altas concentraciones.
- **VOC**: Compuestos orgánicos volátiles, que pueden afectar la salud a niveles altos.

## 5. Resolución de Problemas

- **No Puedo Ver los Datos**: Asegúrese de que el simulador está corriendo y que la API Flask está ejecutándose en el puerto correcto.
- **Datos Repetitivos**: El simulador genera nuevos valores cada 5 segundos. Espere y consulte nuevamente para ver valores diferentes.
