<?php
// layout do cabeçalho

$page_title = "Listagem de Usuários";

include_once "fachada.php";

// procura usuários

$dao = $factory->getUsuarioDao();
$usuarios = $dao->buscaTodos();

?>

<!DOCTYPE HTML>

<html lang=pt-br>

<head>
	<meta charset="UTF-8">
	<title><?php echo $page_title; ?></title>
	
<style>
table td {
    border:1px solid #000000;
}
</style>

</head>

<body>

	<header>
		<h1><?=$page_title?></h1>
	</header>


<?php


// display the products if there are any
if($usuarios) {
//if($total_rows>0){
 
	echo "<table>\n";
	echo "<tr>\n";
		echo "<th>Id</th>\n";
		echo "<th>Login</th>\n";
		echo "<th>Nome</th>\n";
	echo "</tr>\n";

	while ($row = $usuarios->fetch(PDO::FETCH_ASSOC)){

		extract($row);

		echo "<tr>\n";
			echo "<td>{$id}</td>\n";
			echo "<td>{$login}</td>\n";
			echo "<td>{$nome}</td>\n";
		echo "</tr>\n";
	}
	echo "</table>\n";
}
 

?>

</body>
</html>
