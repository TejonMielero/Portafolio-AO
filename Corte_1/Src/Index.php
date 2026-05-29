<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Monitoreo de Invernadero</title>
    <style>
       
        body {
            margin: 0;
            font-family: 'Segoe UI', sans-serif;
            /* Asegúrate de tener una imagen llamada fondo_plantas.jpg en tu carpeta */
            background: #e8f5e9 url("fondo_plantas.jpg") no-repeat center center fixed;
            background-size: cover;
        }

        .overlay {
            background: rgba(0, 0, 0, 0.3); /* Un poco más oscuro para que resalte la tarjeta */
            backdrop-filter: blur(8px);
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .card {
            background: rgba(255, 255, 255, 0.95);
            padding: 40px;
            width: 420px;
            border-radius: 30px;
            box-shadow: 0 15px 35px rgba(0,0,0,0.3);
            text-align: center;
            position: relative;
        }

        .planta-icono {
            width: 100px;
            height: 100px;
            background-color: white;
            border-radius: 50%;
            position: absolute;
            top: -50px;
            left: calc(50% - 50px);
            box-shadow: 0 8px 15px rgba(0,0,0,0.2);
            object-fit: cover;
            border: 4px solid white;
        }

        h1 { 
            color: #2e7d32; 
            margin-top: 50px; 
            font-size: 26px; 
            font-weight: 700;
        }

        p { 
            color: #666; 
            margin-bottom: 30px; 
            font-size: 14px;
        }
        
        input[type="text"] {
            width: 100%; 
            padding: 15px; 
            border-radius: 12px;
            border: 2px solid #e0e0e0; 
            margin-bottom: 20px; 
            box-sizing: border-box;
            font-size: 16px;
            outline: none;
            transition: border-color 0.3s;
        }

        input[type="text"]:focus {
            border-color: #2e7d32;
        }

        button {
            width: 100%; 
            padding: 15px; 
            background: #2e7d32; 
            color: white;
            border: none; 
            border-radius: 12px; 
            cursor: pointer;
            font-weight: bold; 
            font-size: 16px; 
            transition: all 0.3s ease;
            box-shadow: 0 4px 10px rgba(46, 125, 50, 0.3);
        }

        button:hover { 
            background: #1b5e20; 
            transform: translateY(-2px);
            box-shadow: 0 6px 15px rgba(46, 125, 50, 0.4);
        }

        .hint {
            font-size: 11px;
            color: #999;
            margin-top: 15px;
        }
    </style>
</head>
<body>
<div class="overlay">
    <div class="card">
        <div style="font-size: 50px;">🌿</div> 
        <h1>Smart Greenhouse</h1>
        <p>Sistema de Monitoreo de Plantas</p>

        <form action="Procesar.php" method="POST">
            <input type="text" name="criterio" placeholder="Busca 'Temperatura' o '0%'" required 
                   style="width: 100%; padding: 10px; margin: 10px 0;">
            <button type="submit" style="width: 100%; padding: 10px; background: #2e7d32; color: white; border: none; cursor: pointer;">
                BUSCAR DATOS
            </button>
        </form>
    </div>
</div>