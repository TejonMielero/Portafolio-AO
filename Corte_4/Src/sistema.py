import pandas as pd
import time
import os

def cargar_datos(ruta):
   
    inicio = time.time()
   
    df = pd.read_csv(ruta) if ruta.endswith('.csv') else pd.read_json(ruta, lines=True)
    return df, (time.time() - inicio)

def sistema_monitoreo():
    print("=== SISTEMA DE MONITOREO Y ANÁLISIS DE INTERFERENCIAS ===")
    nombre = input("Nombre del archivo (ej. dataset_1M): ")
    formato = input("Formato (csv/json): ").lower()
    ruta = f"Datos/{nombre}.{formato}"
    
    if not os.path.exists(ruta):
        print(f"Error: {ruta} no encontrado. Asegúrese de haber generado los datos.")
        return

    
    df, tiempo = cargar_datos(ruta)
    
    while True:
        print(f"\n--- MENÚ PRINCIPAL ({nombre}) ---")
        print("1. Reporte de Integridad | 2. Buscar evento por ID (Índice) | 3. Agregar evento | 4. Salir")
        op = input("Seleccione opción: ")

        if op == '1': 
            ruido = (df['hall_digital'].sum() / len(df)) * 100
            print(f"\n--- REPORTE TÉCNICO ---")
            print(f"Tiempo de carga: {tiempo:.4f}s")
            print(f"Total de muestras: {len(df):,}")
            print(f"Degradación del espectro: {ruido:.2f}%")
            print(f"Estado: {'ALERTA' if ruido > 10 else 'SEGURO'}")
        
        elif op == '2':
            try:
                idx = int(input(f"Ingrese índice del evento (0 a {len(df)-1}): "))
                print("\n--- DETALLE DEL REGISTRO ---")
                print(df.iloc[idx])
            except (ValueError, IndexError):
                print("¡Error! Índice inválido.")
            
        elif op == '3':
            print("Ingrese los datos del nuevo evento:")
            nuevo = {
                'luz': float(input("Luz: ")), 
                'voltaje': float(input("Voltaje: ")), 
                'hall_digital': int(input("Hall (0/1): "))
            }
            df_nuevo = pd.DataFrame([nuevo])
            
           
            if formato == 'csv':
                df_nuevo.to_csv(ruta, mode='a', header=False, index=False)
            else:
                with open(ruta, 'a') as f: 
                    f.write('\n' + df_nuevo.to_json(orient='records', lines=True))
            print("¡Evento registrado correctamente en el sistema!")
            
        else: 
            print("Saliendo del sistema...")
            break

if __name__ == "__main__":
    sistema_monitoreo()