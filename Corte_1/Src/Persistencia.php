<?php


$buscar = trim(file_get_contents("busqueda.txt"));


if ($buscar == "") {
    header("Location: Index.html");
    exit();
}


$lineas = file("maestro.txt");
$total = count($lineas); 
$encontrados = "";


for ($i = 0; $i < $total; $i++) {
    
    $renglon = $lineas[$i];

    if (stripos($renglon, $buscar) !== false) {
   
        $encontrados = $encontrados . $renglon; 
    }
}


file_put_contents("filtrado.txt", $encontrados);


header("Location: Tabla.php");
?>