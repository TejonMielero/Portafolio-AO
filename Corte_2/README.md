# Sistema IoT de Control Térmico (Raspberry Pi Pico W)

Proyecto de monitoreo y control automático de temperatura utilizando un sistema embebido, diseñado para gestionar un ventilador de 12V mediante lógica IoT y una interfaz visual inspirada en LabVIEW.

## Descripción General
El sistema utiliza una **Raspberry Pi Pico W** para medir la temperatura con un sensor **DS18B20** y actuar sobre un relé cuando se supera un umbral definido. Los datos son enviados a un servidor web central para su almacenamiento y visualización en tiempo real, aplicando principios de Internet de las Cosas (IoT).

## 🛠 Arquitectura del Sistema
* **Hardware:**
    * **Controlador:** Raspberry Pi Pico W.
    * **Sensor:** DS18B20 (temperatura).
    * **Potencia:** Relé de 5V controlado mediante transistor (amplificación) y diodo de protección.
    * **Estabilidad:** Resistencia pull-up de 1k para señales de control.
* **Software:**
    * **Firmware:** MicroPython en la Pico W.
    * **Backend:** PHP para recepción (JSON), registro de auditoría (`auditoria.txt`) y consulta de datos.
    * **Frontend:** Dashboard interactivo con `Chart.js` y `canvas-gauges`.

##  Flujo de Trabajo
1. **Captura:** La Pico W mide la temperatura cada segundo.
2. **Control:** El sistema activa el relé si la temperatura supera el umbral configurado en `config.json`.
3. **Comunicación:** Los datos se envían al servidor mediante una petición `POST` (JSON).
4. **Visualización:** El dashboard recupera las últimas 20 lecturas para graficar la tendencia y mostrar el estado del ventilador.

## Configuración (config.json)
El sistema permite ajustar parámetros sin recompilar el código mediante un archivo de configuración[cite: 2]:
* `wifi_ssid` / `wifi_pass`: Credenciales de red.
* `umbral_temp`: Temperatura límite para activación.
* `pines`: Definición de puertos GPIO para sensor y relé.

---
*Proyecto de la unidad 3: "Administración y Organización de Datos", Instituto Tecnológico Superior de Lerdo, 2026.*