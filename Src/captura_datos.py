import serial
import csv
import os


if not os.path.exists('Datos'):
    os.makedirs('Datos')

try:
    ser = serial.Serial('COM5', 115200, timeout=2)
    print("Conexión establecida en COM5...")
except Exception as e:
    print(f"Error al conectar: {e}")
    exit()

# 3. Captura
print("Capturando datos (luz, voltaje, hall)... Presiona Ctrl+C para detener.")

with open('Datos/reales.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['luz', 'voltaje', 'hall_digital']) 
    try:
        while True:
            linea = ser.readline().decode('utf-8', errors='ignore').strip()
            
            if linea:
                
                datos = linea.split(',')
                
               
                if len(datos) == 3:
                    writer.writerow(datos)
                    print(f"Guardado: {datos}")
                else:
                  
                    pass
                    
    except KeyboardInterrupt:
        print("\nCaptura terminada. Archivo 'Datos/reales.csv' guardado.")
    finally:
        ser.close()