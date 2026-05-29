<?php

// 1. Abrimos el papelito donde guardamos lo que el usuario quiere buscar
$buscar = trim(file_get_contents("busqueda.txt"));

// 2. Si el usuario no escribio nada, lo mandamos de regreso al inicio
if ($buscar == "") {
    header("Location: Index.html");
    exit();
}

// 3. Jalamos todos los datos que la Raspberry guardo en el maestro
$lineas = file("maestro.txt");
$total = count($lineas); // Contamos cuantos registros hay en total
$encontrados = ""; // Aqui vamos a ir amontonando lo que si coincida

// 4. EL FAMOSO CICLO FOR (Para revisar linea por linea)
for ($i = 0; $i < $total; $i++) {
    
    // Agarramos el renglon que nos toca segun el numero de $i
    $renglon = $lineas[$i];

    // Aqui esta el truco: buscamos si el numero o palabra esta en este renglon
    // Usamos strpos para que sea mas exacto con los numeros
    if (stripos($renglon, $buscar) !== false) {
        // Si lo encontramos, lo pegamos a nuestra lista de encontrados
        $encontrados = $encontrados . $renglon; 
    }
}

// 5. PERSISTENCIA: Guardamos los resultados en un archivo nuevo llamado filtrado.txt
// Esto es lo que pide el profe para que los datos no se pierdan
file_put_contents("filtrado.txt", $encontrados);

// 6. Ya que terminamos la chamba, mandamos al usuario a la tabla para que vea los datos
header("Location: Tabla.php");
?>