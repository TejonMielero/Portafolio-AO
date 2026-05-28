import os
import pandas as pd
import matplotlib.pyplot as plt


plt.style.use('dark_background')
plt.rcParams['axes.facecolor'] = '#121212'
plt.rcParams['grid.color'] = '#2A2A2A'

def generar_graficas(ruta_csv):
    df = pd.read_csv(ruta_csv)
    
  
    plt.figure(figsize=(10, 4))
    plt.plot(df["luz"][:300], color='#00E676', linewidth=1.2)
    plt.title("Monitoreo de Luz - Canal 01", fontsize=14, color='#00E676')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.savefig("Graficas/lineas_osciloscopio.png", dpi=300)
    plt.close()
    
    # 2. HISTOGRAMA (Voltaje)
    plt.figure(figsize=(8, 5))
    plt.hist(df["voltaje"], bins=40, color='#6200EA', edgecolor='white', linewidth=0.5, alpha=0.7)
    plt.title("Distribución de Voltaje", fontsize=14)
    plt.savefig("Graficas/histograma_voltaje.png", dpi=300)
    plt.close()

   
    plt.figure(figsize=(6, 6))
    conteo = df["hall_digital"].value_counts()
    conteo.plot(kind="pie", labels=['Normal', 'Alerta'], autopct="%1.1f%%", colors=['#00E676', '#FF4500'])
    plt.title("Estado de Señal (Hall)")
    plt.ylabel("")
    plt.savefig("Graficas/pastel_estado.png", dpi=300)
    plt.close()

    plt.figure(figsize=(8, 5))
    conteo.plot(kind="bar", color='#00E676')
    plt.title("Frecuencia de Interferencias", fontsize=14)
    plt.savefig("Graficas/barras_interferencias.png", dpi=300)
    plt.close()

    print("¡Gráficas rediseñadas y completas generadas en /Graficas!")

if __name__ == "__main__":
    if not os.path.exists("Graficas"): os.makedirs("Graficas")
    generar_graficas("Reportes/dataset_1M.csv")