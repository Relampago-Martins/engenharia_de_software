<?php
include_once "../fachada.php";
?>

<!DOCTYPE HTML>

<html lang=pt-BR>

	<head>
		<meta charset="UTF-8">

		<style>
			table, th, td {
				border: 1px solid black;
			}
			table.center {
				margin-left: auto;
				margin-right: auto;
			}
		</style>

		<title>Lista de Veículos</title>
	</head>

	<body>

	<h1>Lista de veículos</h1>

	<?php

	echo "<section>";

	// procura usuários

	$dao = $factory->getVeiculoDAO();
	$veiculos = $dao->buscaTodos();


	// mostra os usuários, se tiver
	if($veiculos) {
	
		echo "<table>";
		echo "<tr>";
			echo "<th>Cor</th>";
			echo "<th>Placa</th>";
			echo "<th>Nome</th>";
			echo "<th>Excluir</th>";
		echo "</tr>";

		//while ($row = $usuarios->fetch(PDO::FETCH_ASSOC)){
		//	extract($row);

		foreach ($veiculos as $veiculo) {

			echo "<tr>";
				echo "<td>";
				// link para editar um usuário
				echo "<a href='editaVeiculo.php?id={$veiculo->getId()}'>{$veiculo->getCor()}</a>";
				echo "</td>";
				echo "<td>{$veiculo->getPlaca()}</td>";
				echo "<td>{$veiculo->getNome()}</td>";
				echo "<td>";
				// link para excluir um usuário
				echo "<a href='excluiVeiculo.php?id={$veiculo->getId()}' onclick=\"return confirm('Quer mesmo excluir?');\">X</a>";
				echo "</td>";
	
			echo "</tr>";
		}
		echo "</table>";
	} else {
		echo "<p>Não foram encontrados registros";
	}
	
	echo "</section>";


	?>
	<section>
	<h1>Informações do banco de dados:</h1>
	Driver : <?=$dao->getDriver()?><br>
	Versão do servidor  : <?=$dao->getServerVersion()?><br>
	Versão da lib  : <?=$dao->getClientVersion()?><br>
	</section>

	<br>
	<a href="editaUsuario.php">Novo</a>

	</body>
</html>