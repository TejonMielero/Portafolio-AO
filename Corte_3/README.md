# Análisis de Datos: Ventas de Hardware IoT

Este proyecto se centra en la **ciencia de datos aplicada al comercio electrónico de componentes tecnológicos**. El objetivo es transformar registros brutos de ventas (formato CSV) en información estratégica mediante técnicas de procesamiento jerárquico y visualización gráfica.

##  Descripción del Proyecto
El sistema utiliza el poder de **Python** para convertir archivos `ventas_tecnologia.csv` en tableros de información. El análisis permite identificar patrones de consumo de hardware, detectar los productos más rentables y determinar las temporadas de mayor demanda para la toma de decisiones estratégicas.

## Tecnologías Utilizadas
* **Lenguaje:** Python 3.14.0
* **Procesamiento de Datos:** `Pandas` (limpieza, filtrado y estructuración de datos).
* **Visualización:** `Matplotlib` (generación de gráficas de barras, tendencias de mercado y análisis temporal).
* **Entorno:** Notebooks/Scripts de Python para la manipulación de datasets.

## Análisis Realizado
1. **Limpieza de Datos:** Transformación de registros crudos en datos estructurados (ID, Fecha, Producto, Categoría, Ventas, Cantidad, Mes).
2. **Jerarquización:** Organización de los datos para entender qué productos (ej. Raspberry Pi 5 vs. Cables/Sensores) generan mayor margen de utilidad vs. volumen de ventas.
3. **Identificación de Oportunidades:** Análisis temporal que revela que los meses de **marzo, abril y mayo** presentan picos críticos de demanda, ideales para campañas de mantenimiento o reposición de stock.

## Conclusiones Clave
* **Estrategia de Stock:** Se identificó que, aunque los microcontroladores (ESP32/Pico) tienen un volumen de ventas saludable, la **Raspberry Pi 5** es el producto estrella en cuanto a generación de ingresos.
* **Oportunidad de Crecimiento:** Existe un mercado potencial en la promoción de kits de visión artificial y módulos IoT (LoRa) antes del cierre del semestre académico.

---
*Proyecto de la unidad 4: "Visualización de Datos", Instituto Tecnológico Superior de Lerdo, Semestre Enero-Junio 2026.*