<!doctype html>
<?php
include_once("Veiculo.php");

$id = @$_GET["id"];

$oVeiculo = null;

foreach($veiculos as $cada) {
    if($cada->getId()==$id){
       $oVeiculo = $cada; 
    }
}
if($oVeiculo===null) {
    $oVeiculo = new Veiculo(null, null, null, null);
}

?>

<html>
<head>
  <title>Veículos</title> 
  <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Veículo id = <?=$oVeiculo->getId()?> (detalhes.php)</h1>
    <p><?=$oVeiculo->getNome()?></p>
    <p><?=$oVeiculo->getPlaca()?></p>
    <p><?=$oVeiculo->getMarca()?></p>
    <br>
    <ul>
    	<li>
    		<a href="mostra.php">Voltar</a>
    	</li>
    </ul>
</body>
</html>
