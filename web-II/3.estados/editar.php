<!DOCTYPE html>
<?php
include_once("estado.php");
include_once("utils.php");


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


<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="style.css">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Editar <?=$estado->getId()?></title>
</head> 
<body>
<h1>Editar <?=$estado->getNome()?></h1>
    
    <form 
        action="mostrar-alteracao.php"
        method="GET"
        style="display:flex; flex-direction:column; gap: 16px"
    
    >
        <div>
            <input type="number" name="id" value="<?php echo $estado->getId();?>" hidden/>
        </div>
        <div>
            <label for="Nome">Nome</label>
            <input type="text" name="nome" value="<?php echo $estado->getNome();?>"/>
        </div>

        <div>
            <label for="Sigla">Sigla</label>
            <input type="text" name="sigla" value="<?php echo $estado->getSigla();?>"/>
        </div>

        <button
            type="submit"
        >
            Salvar
        </button>
    </form>

</body>
</html>