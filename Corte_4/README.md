# Informe Técnico: Análisis de Escalabilidad en Almacenamiento de Datos de Señales de Campo

## 1. Introducción
Este proyecto documenta la evaluación de eficiencia en el manejo de archivos (CSV vs JSON) para un sistema de adquisición y monitoreo de señales críticas de campo. El experimento analiza el comportamiento de un sistema embebido midiendo variables físicas reales (Efecto Hall, voltajes y luz), escalando los datos hasta un volumen de 20 millones de registros para validar la robustez de la arquitectura.

## 2. Metodología Experimental
* **Captura de Datos:** Adquisición directa desde hardware (ESP32) a 115200 baudios, integrando sensores de efecto Hall y voltímetros de alta precisión.
* **Procesamiento:** Implementación de scripts en Python (Pandas y NumPy) para la generación de volúmenes masivos (1M, 10M, 20M), aplicando muestreo estadístico basado en el comportamiento de las señales reales.
* **Implementación:** Desarrollo de un sistema central de gestión (CRUD) diseñado para carga eficiente, búsqueda indexada, inserción en modo *append* y generación de reportes automáticos.

## 3. Resultados y Comparativas
Se evaluó el desempeño operativo bajo estrés de los formatos CSV y JSON. La siguiente tabla resume la escalabilidad del sistema:

| Cantidad | Formato | Escritura (s) | Lectura (s) | Tamaño (MB) |
| :--- | :--- | :--- | :--- | :--- |
| 20M | CSV | 305.99 | 37.17 | 1543.72 |
| 20M | JSON | 624.33 | 67.23 | 4004.19 |

El análisis confirma que el formato CSV es el estándar óptimo para el registro de señales masivas debido a su baja latencia y menor huella en almacenamiento.

## 4. Visualización de Datos
El sistema automatiza la generación de evidencias gráficas (ubicadas en `/Graficas`):
* **Líneas:** Comportamiento del canal de luz (monitoreo tipo osciloscopio).
* **Histograma:** Distribución de estabilidad de voltaje.
* **Pastel/Barras:** Análisis de frecuencia de eventos críticos (señal Hall).

## 5. Análisis de Resultados (Fase VI)
Se desarrollaron reportes técnicos en `/Reportes` para la interpretación de señales:
* **Frecuencias:** Clasificación de estados "Normal" vs "Alerta" según el sensor Hall.
* **Análisis Estadístico:** Cálculo preciso de medias, máximos y mínimos de las variables físicas.
* **Detección de Patrones:** Identificación de nodos o intervalos con mayor inestabilidad eléctrica.

## 6. Conclusiones
* **Rendimiento:** El CSV supera al JSON en velocidad de acceso y ahorro de recursos, siendo la opción ideal para sistemas que operan en tiempo real en campo.
* **Operatividad:** Aunque el JSON ofrece flexibilidad estructural, su sobrecarga de metadatos lo hace ineficiente para registros de alta frecuencia.
* **Conclusión Técnica:** La selección de una organización de archivos plana y directa es determinante para la escalabilidad de cualquier sistema de monitoreo de señales industriales.

---
**Autor:** Héctor Iván Rodarte  
**Tecnologías:** Python, Pandas, Matplotlib, NumPy, PySerial, CSV, JSON, Git.