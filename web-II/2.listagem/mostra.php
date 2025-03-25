<!doctype html>
<?php
include_once("Veiculo.php");
?>

<html>
<head>
  <title>Veículos</title> 
  <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Veículos (mostra.php)</h1>
    <?php
        echo "<ul>";
        foreach($veiculos as $cada) {
            echo "<li><a href=\"detalhes.php?id=" . $cada->getId() . "\">" . $cada->getNome() . "</a></li>";
        }
        echo "</ul>";

    ?>
</body>
</html>
