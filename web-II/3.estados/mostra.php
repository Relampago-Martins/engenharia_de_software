<!doctype html>
<?php
include_once("estado.php");
?>

<html>
<head>
  <title>Estados</title> 
  <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Estados</h1>
    <?php
        echo "<ul>";
        foreach($estados as $estado) {
            echo "<li><a href=\"detalhe.php?id=" . $estado->getId() . "\">" . $estado->getNome() . "</a></li>";
        }
        echo "</ul>";

    ?>
</body>
</html>
