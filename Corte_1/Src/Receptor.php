<?php

if (isset($_GET['dato'])) {
    
    
    $info_sensor = $_GET['dato'];
    
    
    file_put_contents('maestro.txt', $info_sensor . PHP_EOL, FILE_APPEND);
    
  
    echo "Dato guardado con exito: " . $info_sensor;
}
?>