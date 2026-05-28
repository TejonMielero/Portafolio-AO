import pandas as pd
import numpy as np
import os

def generar_dataset_completo(archivo_origen, cantidad, nombre_base):

    if not os.path.exists('Datos'):
        os.makedirs('Datos')
    
   
    print(f"\n--- Generando {nombre_base} ---")
    
    
    if os.path.exists(archivo_origen):
        df_semilla = pd.read_csv(archivo_origen)
        media_luz, std_luz = df_semilla['luz'].mean(), df_semilla['luz'].std()
        media_volt, std_volt = df_semilla['voltaje'].mean(), df_semilla['voltaje'].std()
    else:
     
        media_luz, std_luz, media_volt, std_volt = 2000, 50, 3.3, 0.1

    data = {
        'luz': np.random.normal(media_luz, std_luz, cantidad),
        'voltaje': np.random.normal(media_volt, std_volt, cantidad),
        'hall_digital': np.random.choice([0, 1], cantidad, p=[0.95, 0.05])
    }
    
    df = pd.DataFrame(data)
    
   
    csv_path = f'Datos/{nombre_base}.csv'
    df.to_csv(csv_path, index=False)
    print(f"-> Guardado: {csv_path}")
    

    json_path = f'Datos/{nombre_base}.json'
    df.to_json(json_path, orient='records', lines=True)
    print(f"-> Guardado: {json_path}")

if __name__ == "__main__":
    archivo_base = 'Datos/reales.csv'
    
    # Ejecutamos para los tres volúmenes
    generar_dataset_completo(archivo_base, 1000000, 'dataset_1M')
    generar_dataset_completo(archivo_base, 10000000, 'dataset_10M')
    generar_dataset_completo(archivo_base, 20000000, 'dataset_20M')
    
    print("Todos los archivos CSV y JSON están listos/.")