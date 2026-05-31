<?php
// Recibir datos en formato JSON
$data = json_decode(file_get_contents("php://input"), true);


if ($data) {
  
    $line = date("Y-m-d H:i:s") . " - Temp:" . $data['temperatura'] . "°C - " . $data['rele'] . "\n";

    // Guardar en auditoria.txt
    file_put_contents("auditoria.txt", $line, FILE_APPEND);


    http_response_code(200);
    echo "OK";
} else {
    // Si no llegaron datos válidos, mandar error
    http_response_code(400);
    echo "Error: datos inválidos";
}
?>