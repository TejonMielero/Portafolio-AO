<?php
// Paso 1: Recibir el dato del formulario
$dato_sucio = $_POST['criterio'];

// Paso 2: Limpiar espacios extras para que el buscador no se confunda
$dato_limpio = trim($dato_sucio);

// Paso 3: Guardar el numero o palabra en busqueda.txt
file_put_contents("busqueda.txt", $dato_limpio);

// Paso 4: Brincar al archivo que hace la persistencia
header("Location: Persistencia.php");
?>