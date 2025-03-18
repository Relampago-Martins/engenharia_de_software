<?php
 
$num01 = @$_GET["txtNumero1"];
$num02 = @$_GET["txtNumero2"];
$opera = @$_GET["selectOperacao"];

$resul = "";
 
if($num01!=null  && $num02!=null){
  switch($opera){
    case "+":
      $resul = ($num01 + $num02);
    break;
    case "-":
      $resul = ($num01 - $num02);
    break;
    case "*":
      $resul = ($num01 * $num02);
    break;
    case "/":
      $resul = ($num01 / $num02);
    break;
  }

  if ($resul > 20){
    $resul += 8; 
  } else{
    $resul -= 5;
  }
}
 
?>
 
 <!DOCTYPE html>
 <html lang="pt-BR" dir="ltr">
   <head>
     <meta charset="utf-8">
     <title>Operações</title>
     <style>
      input, select{padding:10px; margin: 5px;}
     </style>
   </head>
   <body>
     <h1><?=$resul;?></h1>
     <form method="get">
       <label>Número 1: <input type="text" name="txtNumero1" value="<?php echo $num01;?>"/></label><br>
       <label>Número 2: <input type="text" name="txtNumero2" value="<?php echo $num02;?>"/></label><br>
       <label>Operação:
         <select name="selectOperacao">
           <option value="+">Adição</option>
           <option value="-">Subtração</option>
           <option value="*">Multiplicação</option>
           <option value="/">Divisão</option>
         </select>
       </label><br>
       <input type="submit" name="btnCalcular" value="Calcular">
     </form>
   </body>
 </html>	

