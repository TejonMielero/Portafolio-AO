# 🌿 Sistema Smart Greenhouse (Hardware Real)

Este proyecto presenta una solución de **agricultura de precisión** basada en hardware embebido. El sistema utiliza una **Raspberry Pi Pico W** para capturar datos en tiempo real de sensores físicos, procesar la información y visualizar el estado del invernadero a través de una interfaz web local.

## Descripción del Proyecto
El sistema fue diseñado para monitorear variables críticas de un invernadero real: **temperatura, humedad y niveles de agua**. A diferencia de simulaciones, este sistema interactúa directamente con el entorno mediante sensores físicos conectados a los pines GPIO de la Raspberry Pi Pico W, permitiendo una toma de decisiones basada en datos reales.

## Arquitectura de Hardware y Software
* **Microcontrolador:** Raspberry Pi Pico W (utilizando el chip RP2040).
* **Firmware:** MicroPython.
* **Sensores:** Sensores físicos integrados para medición de variables ambientales.
* **Conectividad:** Servidor web embebido que sirve la interfaz directamente desde la memoria flash del Pico W.
* **Persistencia:** Sistema de archivos interno para el registro histórico de las mediciones de los sensores.

## Características Técnicas
* **Monitoreo Multivariable:** Captura precisa de temperatura, humedad y nivel de agua.
* **Semáforo de Estados:** Clasificación lógica en tiempo real: **Activo, Alerta o Inactivo** según los umbrales configurados.
* **Servidor Web Embebido:** Interfaz intuitiva servida mediante sockets, accesible desde cualquier dispositivo conectado a la misma red Wi-Fi del Pico W.
* **Procesamiento Local:** Toda la lógica de filtrado y gestión de datos ocurre en el dispositivo, garantizando autonomía operativa.

## Flujo de Operación
1. **Captura:** Los sensores físicos envían señales analógicas/digitales a los pines del Pico W.
2. **Procesamiento:** El script en `main.py` (MicroPython) interpreta los voltajes, los convierte a unidades de medida y clasifica el estado del sensor.
3. **Registro:** Los datos se guardan en la memoria local (LittleFS) bajo una estructura de archivo maestro.
4. **Visualización:** El usuario accede vía navegador a la IP del Pico W, donde se genera una tabla dinámica con los resultados actuales.

## Requisitos de Implementación
* **Hardware:**
    * Raspberry Pi Pico W.
    * Sensores compatibles (Temperatura/Humedad/Nivel de agua).
    * Protoboard y cables de conexión.
* **Software:**
    * **Thonny IDE** (para programar la Pico W).
    * Firmware de **MicroPython** instalado en la placa.
    * Bibliotecas de red y manejo de sensores (ej. `machine`, `network`, `usocket`).

---
*Proyecto de Hardware Real e Internet de las Cosas (IoT) - Instituto Tecnológico Superior de Lerdo, 2026.*