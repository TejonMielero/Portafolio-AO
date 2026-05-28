import pandas as pd
import os

def generar_reportes_tecnicos(ruta_csv):
    df = pd.read_csv(ruta_csv)
    if not os.path.exists("reportes"): os.makedirs("reportes")
    
    # Reporte 1: Frecuencia de estados
    df['hall_digital'].value_counts().to_csv('reportes/frecuencia_hall.csv')
    
    # Reporte 2: Análisis descriptivo (Promedios, máximos, mínimos de luz y voltaje)
    df[['luz', 'voltaje']].describe().to_csv('reportes/analisis_descriptivo.csv')
    
    
    df.groupby('hall_digital')['voltaje'].mean().to_csv('reportes/voltaje_promedio_por_estado.csv')
    
    print("Reportes técnicos generados. Ya tienes tus archivos tabulares.")

generar_reportes_tecnicos("Datos/dataset_1M.csv")