<?php

error_reporting(E_ERROR | E_PARSE);

include_once('model/Usuario.php');
include_once('model/veiculo.php');
include_once('dao/DAO.php');
include_once('dao/UsuarioDao.php');
include_once('dao/VeiculoDao.php');
include_once('dao/DaoFactory.php');
include_once('dao/postgres/PostgresDaoFactory.php');

$factory = new PostgresDaofactory();

?>
