<!doctype html>
<?php
include_once("estado.php");

$id = @$_GET["id"];

$estado = null;
    
foreach($estados as $std) {
    if($std->getId()==$id){
        $estado = $std; 
    }
}
if($estado===null) {
    $estado = new Estado(null, null, null, null);
}

?>

<html>
<head>
  <title><?=$estado->getNome()?></title> 
  <link rel="stylesheet" href="style.css">
</head>
<body>

    <h1>Estado id = <?=$estado->getId()?></h1>
    
    <p><?=$estado->getNome()?></p>
    <p><?=$estado->getSigla()?></p>
    <br>
    <ul>
        <li>
    		<a href="editar.php?id=<?=$id?>">Editar</a>
    	</li>
    	<li>
    		<a href="mostra.php">Voltar</a>
    	</li>
    </ul>
</body>
</html>
