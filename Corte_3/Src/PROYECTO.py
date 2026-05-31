import pandas as pd
import matplotlib.pyplot as plt

# --- PARTE 1: LECTURA Y PROCESAMIENTO ---
def ejecutar_analisis():
    
    try:
        df = pd.read_csv('ventas_tecnologia.csv')
    except FileNotFoundError:
        print("Error: No se encontró el archivo 'ventas_tecnologia.csv'")
        return

    print("--- REPORTE DE VENTAS POR PRODUCTO ---")
    ventas_producto = df.groupby('Producto')['Ventas'].sum().sort_values(ascending=False)
    print(ventas_producto)
    print("\n--- REPORTE DE VENTAS POR MES ---")
    
    orden_meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio']
    ventas_mes = df.groupby('Mes')['Ventas'].sum().reindex(orden_meses)
    print(ventas_mes)

    # --- PARTE 2: VISUALIZACIONES (Matplotlib) ---
    
    plt.figure(figsize=(12, 7))
    ventas_producto.plot(kind='bar', color='skyblue')
    plt.title("Ingresos Totales por Activo IoT")
    plt.xlabel("Producto")
    plt.ylabel("Ingresos ($)")

    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show() 

   
    plt.figure(figsize=(10, 6))
    ventas_mes.plot(kind='line', marker='o', linewidth=3, color='red')
    plt.title("Evolución Mensual de Ventas - IoT Hub")
    plt.xlabel("Mes")
    plt.ylabel("Ingresos ($)")
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show() 

  
    plt.figure(figsize=(9, 9))

    ventas_producto.plot(kind='pie', autopct='%1.1f%%', startangle=140, labels=None, cmap='viridis', pctdistance=0.85)
    plt.title("Distribución de Ventas por Activo IoT")
    plt.ylabel("")
  
    plt.legend(labels=ventas_producto.index, loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
    plt.tight_layout()
    plt.show()

    # --- PARTE 3: JERARQUÍA E IMPORTANCIA ---
    top_ingreso = ventas_producto.idxmax()
    peor_vendido = ventas_producto.idxmin()
    mes_rentable = ventas_mes.idxmax()
    
    print("\n--- ANÁLISIS JERÁRQUICO (Toma de Decisiones) ---")
    print(f"1. Producto con mayores ingresos: {top_ingreso}")
    print(f"2. Producto menos vendido (Alerta stock): {peor_vendido}")
    print(f"3. Mes más rentable del semestre: {mes_rentable}")

if __name__ == "__main__":
    ejecutar_analisis()