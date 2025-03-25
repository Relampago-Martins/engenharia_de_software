<!DOCTYPE html>
<?php
include_once("estado.php");
include_once("utils.php");

$id = @$_GET["id"];
$nome = @$_GET["nome"];
$sigla = @$_GET["sigla"];


$estado = new Estado(99, $nome, $sigla);
    

?>


<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="style.css">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Editou <?=$estado->getId()?></title>
</head> 
<body>
    <h1>Editou  <?=$estado->getNome()?></h1>
    
    <p><?=$estado->getNome()?></p>
    <p><?=$estado->getSigla()?></p>
    <br>
    <ul>
        <li>
    		<a href="editar.php?id=<?=$id?>">Editar de novo</a>
    	</li>
    	<li>
    		<a href="mostra.php">Voltar</a>
    	</li>
    </ul>

</body>
</html>