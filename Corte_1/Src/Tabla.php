<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Visualización de Datos</title>
    <style>
        
        body { font-family: 'Segoe UI', sans-serif; background: #e8f5e9 url("fondo_plantas.jpg") no-repeat center center fixed; background-size: cover; margin: 0; padding: 20px; }
        .table-container { background: rgba(255, 255, 255, 0.95); padding: 30px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.2); max-width: 950px; margin: 40px auto; }
        table { width: 100%; border-collapse: collapse; }
        th { background-color: #2e7d32; color: white; padding: 12px; text-align: left; }
        td { padding: 12px; border-bottom: 1px solid #eee; }
        
        
        tr.activo { border-left: 5px solid #4caf50; background: #f1f8e9; }
        tr.alerta { border-left: 5px solid #f44336; background: #ffebee; }
        tr.inactivo { border-left: 5px solid #9e9e9e; background: #f5f5f5; }
        
        .counter { margin-top: 20px; font-weight: bold; color: #2e7d32; text-align: right; }
        .btn-volver { display: inline-block; padding: 10px 20px; background: #2e7d32; color: white; text-decoration: none; border-radius: 10px; margin-bottom: 20px; }
    </style>
</head>
<body>

<div class="table-container">
    <a href="Index.php" class="btn-volver">← Nueva Búsqueda</a>
    
    <table>
        <tr>
            <th>Temperatura</th>
            <th>Humedad</th>
            <th>Nivel de Agua</th>
            <th>Estado Bomba</th>
        </tr>

        <?php
        $contador = 0;
        // El criterio viene de procesar.php
        $busqueda = isset($_GET['busqueda']) ? trim($_GET['busqueda']) : '';
        
        // Según la rúbrica, leemos el resultado del filtrado
        $nombre_archivo = "filtrado.txt"; 

        if(file_exists($nombre_archivo)){
            $lineas = file($nombre_archivo);
            
            // Invertimos para ver lo más nuevo arriba
            foreach(array_reverse($lineas) as $linea){
                $linea = trim($linea);
                if(empty($linea)) continue;

                // lógica de filtrado por texto
                if(empty($busqueda) || stripos($linea, $busqueda) !== false){
                    
                    $datos = explode(",", $linea);
                    
                    // Lógica de ESTADO para tus clases de diseño
                    // Buscamos si la línea dice "ON" para ponerla verde o "0%" para roja
                    $linea_min = strtolower($linea);
                    $clase = "inactivo";
                    
                    if(strpos($linea_min, "on") !== false) $clase = "activo";
                    elseif(strpos($linea_min, "0%") !== false) $clase = "alerta";

                    echo "<tr class='$clase'>";
                    echo "<td>" . ($datos[1] ?? '-') . "</td>"; // Temperatura XX
                    echo "<td>" . ($datos[2] ?? '-') . "</td>"; // Humedad XX
                    echo "<td>" . ($datos[3] ?? '-') . "</td>"; // Nivel de Agua XX
                    echo "<td>" . ($datos[4] ?? '-') . "</td>"; // Bomba: XX
                    echo "</tr>";
                    
                    $contador++;
                }
            }
        } else {
            echo "<tr><td colspan='5' style='text-align:center;'>No hay datos filtrados aún...</td></tr>";
        }
        ?>
    </table>

    <div class="counter">
        <?php echo "Total de registros encontrados: " . $contador; ?>
    </div>
</div>

</body>
</html>